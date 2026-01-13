from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.pipelines.predict_pipeline import CustomData, PredictPipeline

app = FastAPI(title="House Price Prediction API")

# ---------- CORS ----------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- Input Schema ----------
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

# ---------- Health Check ----------
@app.get("/")
def health():
    return {"status": "API is running 🚀"}

# ---------- Prediction Endpoint ----------
@app.post("/predict")
def predict_price(data: HouseData):
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
