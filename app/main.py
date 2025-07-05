from fastapi import FastAPI
from app.model import CarInput
import joblib
import os

app = FastAPI()

model = joblib.load(os.path.join("app", "car_model.pkl"))

@app.post("/predict")
def predict_price(data: CarInput):
    input_data = [[
        data.year,
        data.mileage,
        data.fuel_type,
        data.transmission,
        data.owner
    ]]
    prediction = model.predict(input_data)[0]
    return {"predicted_price": round(prediction, 2)}

