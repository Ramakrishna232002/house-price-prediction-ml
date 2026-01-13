# src/components/data_transformation.py
import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from src.utils.logger import logging
from src.utils.exception import CustomException
import pickle

class DataTransformation:
    def __init__(self):
        self.transformer_path = os.path.join("artifacts", "transformer.pkl")

    def initiate_data_transformation(self, df: pd.DataFrame):
        try:
            logging.info("Data transformation started")

            # Separate features and target
            X = df.drop("price", axis=1)
            y = df["price"]

            # Identify categorical and numerical columns
            numeric_cols = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
            categorical_cols = X.select_dtypes(include=["object"]).columns.tolist()

            # Define Column Transformer
            numeric_transformer = Pipeline(steps=[("scaler", StandardScaler())])
            categorical_transformer = Pipeline(steps=[("onehot", OneHotEncoder(drop="first"))])

            preprocessor = ColumnTransformer(
                transformers=[
                    ("num", numeric_transformer, numeric_cols),
                    ("cat", categorical_transformer, categorical_cols)
                ]
            )

            # Fit & transform
            X_transformed = preprocessor.fit_transform(X)

            # Save transformer for later use
            os.makedirs("artifacts", exist_ok=True)
            with open(self.transformer_path, "wb") as f:
                pickle.dump(preprocessor, f)

            # Split dataset
            X_train, X_test, y_train, y_test = train_test_split(
                X_transformed, y, test_size=0.2, random_state=42
            )

            logging.info("Data transformation completed")
            return X_train, X_test, y_train, y_test, self.transformer_path

        except Exception as e:
            raise CustomException(e, sys)



        

