from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/predict")
async def predict(request: Request):
    # Lire le corps brut (bytes), décoder en utf-8 et strip les espaces
    raw_data = (await request.body()).decode("utf-8").strip()

    # Remplacer la virgule par un point pour la conversion float
    raw_data = raw_data.replace(",", ".")

    try:
        total_value = float(raw_data)
    except ValueError:
        return JSONResponse(status_code=400, content={"error": f"Valeur invalide: '{raw_data}'"})

    # Appeler ta fonction de recherche de combinaison
    result = find_combination(total_value)

    if result is None:
        return {"message": "Aucune combinaison trouvée pour ce total."}
    else:
        return {"result": result}

def find_combination(total):
    # Exemple fictif d'une recherche exacte (à remplacer par ta logique)
    if total == 48.2:
        return [
            "Entrée: salade (10.0 TND)",
            "Plat: couscous (38.2 TND)"
        ]
    if total == 88.2:
        return [
            "Entrée: soupe (15.0 TND)",
            "Plat: tajine (50.0 TND)",
            "Dessert: baklava (23.2 TND)"
        ]
    return None
