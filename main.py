from fastapi import FastAPI, Query
from fastapi.responses import PlainTextResponse

app = FastAPI()

# Menu
entrees = {
    "Salade – Légumes grillés": 13.4,
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

@app.get("/predict", response_class=PlainTextResponse)
def predict(total: str = Query(...)):
    try:
        total = total.replace(",", ".")
        total_float = round(float(total), 3)

        for e_name, e_price in entrees.items():
            for p_name, p_price in plats.items():
                for d_name, d_price in desserts.items():
                    for c_name, c_price in chichas.items():
                        combo_total = round(e_price + p_price + d_price + c_price, 3)
                        if abs(combo_total - total_float) < 0.001:
                            return (
                                f"vous allez choisir :\n"
                                f"{e_name} – {e_price:.3f} TND\n"
                                f"{p_name} – {p_price:.3f} TND\n"
                                f"{d_name} – {d_price:.3f} TND\n"
                                f"{c_name} – {c_price:.3f} TND\n"
                                f"et le totale sera {combo_total:.3f} TND."
                            )
        return "Aucune combinaison trouvée pour ce total."
    except:
        return "Erreur : total invalide."
