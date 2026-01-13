import pandas as pd
import yaml
import os
import sys
from src.utils.logger import logging
from src.utils.exception import CustomException

class DataValidation:
    def __init__(self, schema_path):
        self.schema_path = schema_path

    def read_schema(self):
        try:
            with open(self.schema_path, "r") as file:
                schema = yaml.safe_load(file)
            return schema
        except Exception as e:
            raise CustomException(f"Error reading schema file: {e}", sys)

    def validate_columns(self, df: pd.DataFrame):
        try:
            schema = self.read_schema()
            schema_columns = schema["columns"].keys()
            df_columns = df.columns

            missing_columns = set(schema_columns) - set(df_columns)

            if missing_columns:
                raise CustomException(f"Missing columns: {missing_columns}", sys)

            logging.info("All columns validated successfully")
            return True

        except Exception as e:
            raise CustomException(f"Data validation failed: {e}", sys)

