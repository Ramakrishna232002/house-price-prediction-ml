# app/main.py
import sys
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# -------------------------------
# Fix import path
# -------------------------------
# Add project root to sys.path so Python can find `src`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.pipelines.predict_pipeline import CustomData, PredictPipeline

# -------------------------------
# FastAPI app
# -------------------------------
app = FastAPI(title="House Price Prediction API")

# -------------------------------
# CORS (allow frontend requests)
# -------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace "*" with "http://localhost:3000" for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# Pydantic input schema
# -------------------------------
class HouseData(BaseModel):
    area: int
    bedrooms: int
    bathrooms: int
    stories: int
    parking: int
    mainroad: str
    guestroom: str
    basement: str
    hotwaterheating: str
    airconditioning: str
    prefarea: str
    furnishingstatus: str

# -------------------------------
# Health check endpoint
# -------------------------------
@app.get("/")
def read_root():
    return {"status": "API is running 🚀"}

# -------------------------------
# Prediction endpoint
# -------------------------------
@app.post("/predict")
def predict_price(data: HouseData):
    try:
        input_data = CustomData(
            area=data.area,
            bedrooms=data.bedrooms,
            bathrooms=data.bathrooms,
            stories=data.stories,
            parking=data.parking,
            mainroad=data.mainroad,
            guestroom=data.guestroom,
            basement=data.basement,
            hotwaterheating=data.hotwaterheating,
            airconditioning=data.airconditioning,
            prefarea=data.prefarea,
            furnishingstatus=data.furnishingstatus
        )

        df = input_data.get_data_as_dataframe()
        pipeline = PredictPipeline()
        prediction = pipeline.predict(df)

        return {"predicted_price": float(prediction[0])}
    except Exception as e:
        return {"error": str(e)}


