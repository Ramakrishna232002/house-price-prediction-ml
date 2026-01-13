from src.components.data_transformation import DataTransformation
import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("artifacts/raw_data.csv")

    transformer = DataTransformation()
    X_train, X_test, y_train, y_test, transformer_path = transformer.initiate_data_transformation(df)

    print("✅ Data Transformation Successful!")
    print(f"Transformed train shape: {X_train.shape}")
    print(f"Transformed test shape: {X_test.shape}")
    print(f"Transformer saved at: {transformer_path}")
