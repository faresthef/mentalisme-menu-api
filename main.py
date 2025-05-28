from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

app = FastAPI()

menu = {
    "entrees": {
        "Salade": 13.4,
        "Brik à l'œuf": 8.9,
        "Fricassé Tunisien": 6.6
    },
    "plats": {
        "Couscous au Poulet": 18.1,
        "Kefteji": 24.3,
        "Entrecôte grillée": 21.2
    },
    "desserts": {
        "Tiramisu maison": 8.7,
        "Cheesecake aux fruits rouges": 10.8,
        "Fondant au chocolat": 12.0
    },
    "chichas": {
        "Chicha Apple": 32.5,
        "Chicha Love": 44.2,
        "Chicha Soltan": 53.5
    }
}

@app.post("/predict", response_class=PlainTextResponse)
async def predict(request: Request):
    data = await request.json()
    total_str = data.get("total", "").replace(",", ".")
    try:
        target_total = float(total_str)
    except ValueError:
        return "Erreur : total invalide."

    for e_nom, e_val in menu["entrees"].items():
        for p_nom, p_val in menu["plats"].items():
            for d_nom, d_val in menu["desserts"].items():
                for c_nom, c_val in menu["chichas"].items():
                    somme = round(e_val + p_val + d_val + c_val, 1)
                    if somme == round(target_total, 1):
                        return f"""vous allez choisir :
{e_nom} ({e_val} TND)
{p_nom} ({p_val} TND)
{d_nom} ({d_val} TND)
{c_nom} ({c_val} TND)
et le totale sera {somme} TND."""

    return "Aucune combinaison trouvée pour ce total."
