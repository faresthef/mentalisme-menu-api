from fastapi import FastAPI, Query, HTTPException

app = FastAPI()

@app.get("/predict")
def predict(total: str = Query(..., description="Total de la commande (ex: 65.600 ou 65,600)")):
    try:
        # Accepter les deux formats : 65,600 ou 65.600
        total_value = float(total.replace(",", "."))
    except ValueError:
        raise HTTPException(status_code=422, detail="Format de total invalide")

    # Exemple de logique (à remplacer par ton vrai menu)
    if total_value == 88.200:
        return {
            "entrée": "Fricassé Tunisien",
            "plat": "Entrecôte grillée",
            "dessert": "Tiramisu maison",
            "chicha": "Chicha Soltan"
        }
    else:
        raise HTTPException(status_code=404, detail="Combinaison introuvable")
