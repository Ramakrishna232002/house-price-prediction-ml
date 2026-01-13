import pandas as pd
from src.components.data_validation import DataValidation

df = pd.read_csv("data/raw/Housing.csv")

validator = DataValidation("config/schema.yml")
validator.validate_columns(df)

print("✅ Data Validation Passed")
