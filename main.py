from fastapi import FastAPI, Query

app = FastAPI()

MENU = {
    "entrees": [
        {"name": "Salade", "price": 13.4},
        {"name": "Brik à l'œuf", "price": 8.9},
        {"name": "Fricassé Tunisien", "price": 6.6},
    ],
    "plats": [
        {"name": "Couscous au Poulet", "price": 18.1},
        {"name": "Kefteji", "price": 24.3},
        {"name": "Entrecôte grillée", "price": 21.2},
    ],
    "desserts": [
        {"name": "Tiramisu maison", "price": 8.7},
        {"name": "Cheesecake aux fruits rouges", "price": 10.8},
        {"name": "Fondant au chocolat", "price": 12.0},
    ],
    "chichas": [
        {"name": "Chicha Apple", "price": 32.5},
        {"name": "Chicha Love", "price": 44.2},
        {"name": "Chicha Soltan", "price": 53.5},
    ]
}

@app.get("/predict")
def predict_order(total: float = Query(..., description="Total exact en TND")):
    target = round(total, 1)

    for entree in MENU["entrees"]:
        for plat in MENU["plats"]:
            for dessert in MENU["desserts"]:
                for chicha in MENU["chichas"]:
                    calc_total = round(
                        entree["price"] + plat["price"] + dessert["price"] + chicha["price"], 1
                    )
                    if calc_total == target:
                        return {
                            "entree": entree["name"],
                            "plat": plat["name"],
                            "dessert": dessert["name"],
                            "chicha": chicha["name"],
                            "total": calc_total
                        }

    return {"error": "Aucune combinaison trouvée pour ce total."}
