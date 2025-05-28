from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modèle pour recevoir les données JSON
class RequestData(BaseModel):
    total: str

# Ton menu, avec les prix (les mêmes que tu avais)
entrees = {
    "Salade": 13.400,
    "Brik à l'œuf": 8.900,
    "Fricassé Tunisien": 6.600,
}
plats = {
    "Couscous au Poulet": 18.100,
    "Kefteji": 24.300,
    "Entrecôte grillée": 21.200,
}
desserts = {
    "Tiramisu maison": 8.700,
    "Cheesecake aux fruits rouges": 10.800,
    "Fondant au chocolat": 12.000,
}
chichas = {
    "Chicha Apple": 32.500,
    "Chicha Love": 44.200,
    "Chicha Soltan": 53.500,
}

def trouver_combinaison(total):
    total = float(total.replace(",", "."))  # transforme la chaîne en float
    # recherche brute-force de la combinaison (simplifiée)
    for e, p_e in entrees.items():
        for pl, p_pl in plats.items():
            for d, p_d in desserts.items():
                for c, p_c in chichas.items():
                    if abs(p_e + p_pl + p_d + p_c - total) < 0.01:
                        return (e, p_e, pl, p_pl, d, p_d, c, p_c)
    return None

@app.post("/predict")
async def predict(data: RequestData):
    combo = trouver_combinaison(data.total)
    if combo is None:
        return {"result": "Aucune combinaison trouvée pour ce total."}
    e, p_e, pl, p_pl, d, p_d, c, p_c = combo
    texte = (
        "vous allez choisir :\n"
        f"{e} – {p_e} TND\n"
        f"{pl} – {p_pl} TND\n"
        f"{d} – {p_d} TND\n"
        f"{c} – {p_c} TND\n"
        f"et le totale sera {data.total} TND."
    )
    return {"result": texte}
