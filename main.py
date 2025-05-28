from fastapi import FastAPI, Query
from fastapi.responses import PlainTextResponse

app = FastAPI()

# Exemple menu simplifié pour démo
entrees = {
    "Salade": 13.4,
    "Brik à l'œuf": 8.9,
    "Fricassé Tunisien": 6.6
}
plats = {
    "Couscous au Poulet": 18.1,
    "Kefteji": 24.3,
    "Entrecôte grillée": 21.2
}
desserts = {
    "Tiramisu maison": 8.7,
    "Cheesecake aux fruits rouges": 10.8,
    "Fondant au chocolat": 12.0
}
chichas = {
    "Chicha Apple": 32.5,
    "Chicha Love": 44.2,
    "Chicha Soltan": 53.5
}

def trouver_combinaison(total: float):
    # Remplace par ta vraie logique ici
    # Exemple fixe juste pour test
    return ("Salade", 13.4), ("Couscous au Poulet", 18.1), ("Tiramisu maison", 8.7), ("Chicha Apple", 32.5)

@app.post("/predict")
async def predict(total: float = Query(...)):
    entree, plat, dessert, chicha = trouver_combinaison(total)

    texte = (
        "vous allez choisir :\n"
        f"{entree[0]} {entree[1]} TND\n"
        f"{plat[0]} {plat[1]} TND\n"
        f"{dessert[0]} {dessert[1]} TND\n"
        f"{chicha[0]} {chicha[1]} TND\n"
        f"et le total sera {total} TND."
    )
    return PlainTextResponse(texte)
