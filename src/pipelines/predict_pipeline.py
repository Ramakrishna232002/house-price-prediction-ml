import os
import pickle
import pandas as pd
from src.utils.logger import logging
from src.utils.exception import CustomException

class CustomData:
    """
    This class will take user input (from UI or manually) and convert it into a DataFrame.
    """
    def __init__(self, area, bedrooms, bathrooms, stories, parking,
                 mainroad, guestroom, basement, hotwaterheating,
                 airconditioning, prefarea, furnishingstatus):
        self.area = area
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.stories = stories
        self.parking = parking
        self.mainroad = mainroad
        self.guestroom = guestroom
        self.basement = basement
        self.hotwaterheating = hotwaterheating
        self.airconditioning = airconditioning
        self.prefarea = prefarea
        self.furnishingstatus = furnishingstatus

    def get_data_as_dataframe(self):
        try:
            data_dict = {
                "area": [self.area],
                "bedrooms": [self.bedrooms],
                "bathrooms": [self.bathrooms],
                "stories": [self.stories],
                "parking": [self.parking],
                "mainroad": [self.mainroad],
                "guestroom": [self.guestroom],
                "basement": [self.basement],
                "hotwaterheating": [self.hotwaterheating],
                "airconditioning": [self.airconditioning],
                "prefarea": [self.prefarea],
                "furnishingstatus": [self.furnishingstatus]
            }
            df = pd.DataFrame(data_dict)
            return df
        except Exception as e:
            raise CustomException(e, sys)

class PredictPipeline:
    """
    This class loads the saved transformer and model, 
    applies transformation, and predicts house price.
    """
    def __init__(self):
        self.model_path = os.path.join("artifacts", "model.pkl")
        self.transformer_path = os.path.join("artifacts", "transformer.pkl")

    def predict(self, df: pd.DataFrame):
        try:
            # Load transformer
            with open(self.transformer_path, "rb") as f:
                transformer = pickle.load(f)

            # Transform data
            X = transformer.transform(df)

            # Load model
            with open(self.model_path, "rb") as f:
                model = pickle.load(f)

            # Predict
            preds = model.predict(X)
            return preds
        except Exception as e:
            raise CustomException(e, sys)
