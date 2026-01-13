# src/pipelines/predict_runner.py
from src.pipelines.predict_pipeline import CustomData, PredictPipeline

if __name__ == "__main__":
    # Example input
    input_data = CustomData(
        area=5000,
        bedrooms=3,
        bathrooms=2,
        stories=2,
        parking=1,
        mainroad="yes",
        guestroom="no",
        basement="yes",
        hotwaterheating="no",
        airconditioning="yes",
        prefarea="yes",
        furnishingstatus="semi-furnished"
    )

    df = input_data.get_data_as_dataframe()

    pipeline = PredictPipeline()
    prediction = pipeline.predict(df)

    print(f"🏠 Predicted House Price: {prediction[0]}")

