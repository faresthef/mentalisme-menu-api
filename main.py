from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Menu avec les bons prix
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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
async def predict(total: float = Form(...)):
    total = round(total, 3)

    for e_name, e_price in entrees.items():
        for p_name, p_price in plats.items():
            for d_name, d_price in desserts.items():
                for c_name, c_price in chichas.items():
                    if round(e_price + p_price + d_price + c_price, 3) == total:
                        message = (
                            f"vous allez choisir :\n"
                            f"{e_name} - {e_price:.3f} TND\n"
                            f"{p_name} - {p_price:.3f} TND\n"
                            f"{d_name} - {d_price:.3f} TND\n"
                            f"{c_name} - {c_price:.3f} TND\n"
                            f"et le total sera {total:.3f} TND."
                        )
                        return {"message": message}
    
    return {"message": "Aucune combinaison trouvée pour ce total."}
