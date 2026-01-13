# src/components/model_trainer.py
import os
import sys
import pickle
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from src.utils.logger import logging
from src.utils.exception import CustomException

class ModelTrainer:
    def __init__(self):
        self.model_path = os.path.join("artifacts", "model.pkl")

    def train_model(self, X_train, y_train):
        try:
            logging.info("Model training started")
            model = RandomForestRegressor(n_estimators=100, random_state=42)
            model.fit(X_train, y_train)
            logging.info("Model training completed")
            return model
        except Exception as e:
            raise CustomException(e, sys)

    def evaluate_model(self, model, X_test, y_test):
        try:
            predictions = model.predict(X_test)
            rmse = np.sqrt(mean_squared_error(y_test, predictions))
            r2 = r2_score(y_test, predictions)
            logging.info(f"Model evaluation completed: RMSE={rmse}, R2={r2}")
            return rmse, r2
        except Exception as e:
            raise CustomException(e, sys)

    def save_model(self, model):
        try:
            os.makedirs("artifacts", exist_ok=True)
            with open(self.model_path, "wb") as f:
                pickle.dump(model, f)
            logging.info(f"Model saved at: {self.model_path}")
        except Exception as e:
            raise CustomException(e, sys)
