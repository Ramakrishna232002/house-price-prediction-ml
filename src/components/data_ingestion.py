import os
import sys
import pandas as pd
from src.utils.logger import logger
from src.utils.exception import CustomException

class DataIngestion:
    def __init__(self):
        # Raw data will be saved here
        self.raw_data_path = os.path.join("artifacts", "raw_data.csv")

    def initiate_data_ingestion(self):
        try:
            logger.info("Data ingestion started")

            # Construct path to raw CSV
            raw_file_path = os.path.join("data", "raw", "Housing.csv")
            
            # Read raw data
            df = pd.read_csv(raw_file_path)

            # Create artifacts folder if it doesn't exist
            os.makedirs("artifacts", exist_ok=True)

            # Save a copy to artifacts
            df.to_csv(self.raw_data_path, index=False)

            logger.info("Data ingestion started")

            return df

        except Exception as e:
            raise CustomException(e, sys)

