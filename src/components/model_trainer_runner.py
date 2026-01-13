from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

dt = DataTransformation()
X_train, X_test, y_train, y_test = dt.initiate_data_transformation(
    "data/raw/Housing.csv"
)

trainer = ModelTrainer()
score = trainer.initiate_model_trainer(
    X_train, X_test, y_train, y_test
)

print(f"✅ Model Training Completed | Best R2 Score: {score}")
