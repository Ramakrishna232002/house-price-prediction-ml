import pickle
import pandas as pd
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__ == "__main__":
    # Load raw data
    df = pd.read_csv("artifacts/raw_data.csv")

    # Transform data
    transformer = DataTransformation()
    X_train, X_test, y_train, y_test, transformer_path = transformer.initiate_data_transformation(df)

    # Train model
    trainer = ModelTrainer()
    model = trainer.train_model(X_train, y_train)

    # Evaluate model
    rmse, r2 = trainer.evaluate_model(model, X_test, y_test)
    print(f"✅ Model trained successfully!")
    print(f"RMSE: {rmse:.2f}, R2: {r2:.3f}")

    # Save model
    trainer.save_model(model)
    print(f"Model saved at: {trainer.model_path}")
