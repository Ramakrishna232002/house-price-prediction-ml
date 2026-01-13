from src.components.data_validation import DataValidation
import pandas as pd

if __name__ == "__main__":
    schema_path = "config/schema.yml"
    df = pd.read_csv("artifacts/raw_data.csv")

    validator = DataValidation(schema_path)
    try:
        validator.validate_columns(df)
        print("✅ Data validation successful!")
    except Exception as e:
        print(f"❌ Data validation failed: {e}")
