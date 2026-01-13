# 🏠 House Price Prediction ML Project
 
A full-stack Machine Learning project that predicts house prices based on user inputs.  
It uses a **Python ML backend (FastAPI)** and a **React frontend** for dynamic, interactive predictions.
 
---
 
## � Features
 
- Dynamic React frontend form for user input
- Real-time price prediction via FastAPI backend
- Interactive and responsive UI
- Modular ML pipeline (`predict_pipeline.py`) for preprocessing and prediction
- Easy-to-extend architecture for new features or models
- Fully containerized Python environment with dependency management
 
---
 
## 📁 Project Structure
 
```text
house-price-prediction-ml/
│
├─ app/                       # Backend (FastAPI)
│   ├─ main.py                # FastAPI app & endpoints
│   ├─ src/
│   │   ├─ pipelines/
│   │   │   ├─ predict_pipeline.py  # CustomData & PredictPipeline
│   │   │   └─ training_pipeline.py
│   │   ├─ components/
│   │   ├─ utils/
│   │   ├─ api/
│   │   ├─ App.jsx
│   │   └─ index.jsx
│
├─ frontend/house-price-ui/    # React frontend
│   ├─ src/
│   │   ├─ App.js              # React form & API integration
│   │   ├─ index.js
│   │   └─ App.css
│   ├─ public/
│   ├─ package.json
│   └─ package-lock.json
│
├─ data/                       # Sample or training data
├─ artifacts/                  # ML artifacts (models, scalers)
├─ notebooks/                  # Optional Jupyter notebooks
├─ logs/                       # Logs
├─ requirements.txt            # Python dependencies
└─ README.md                   # Project documentation
```
 
## 🛠 Tech Stack
 
- **Backend**: Python, FastAPI, Pydantic
- **Frontend**: React, JavaScript, HTML, CSS
- **Machine Learning**: scikit-learn / pandas / numpy
- **Deployment / Dev**: Uvicorn, npm
 
## 🚀 Getting Started
 
### 1. Clone the repository
```bash
git clone <your-repo-url>
cd house-price-prediction-ml
```
 
### 2. Backend Setup
```bash
# Navigate to backend folder
cd app
 
# Install Python dependencies
pip install -r requirements.txt
 
# Run FastAPI server
PYTHONPATH=. uvicorn main:app --reload
```
 
### 3. Frontend Setup
```bash
# Navigate to frontend
cd ../frontend/house-price-ui
 
# Install dependencies
npm install
 
# Start React development server
npm start
```
 
## � Usage
 
1. Open the frontend URL in your browser.
2. Fill the house details in the interactive form:
    - Area, Bedrooms, Bathrooms, Stories, Parking
    - Main Road, Guest Room, Basement, Hot Water Heating
    - Air Conditioning, Preferred Area, Furnishing Status
3. Click **Predict Price**.
4. Predicted house price will appear dynamically below the form.
 
## 🧩 ML Pipeline
 
- **CustomData**: Collects user input and converts into Pandas DataFrame.
- **PredictPipeline**: Loads trained model and scaler, applies preprocessing, and returns prediction.
 
Modular pipeline design allows for:
- Adding new features
- Switching ML models
- Training & testing separately
 
## 🎨 Frontend Details
 
- Built using React.
- Fully dynamic form – no hard-coded values.
- Form submission triggers fetch to FastAPI backend.
- Interactive UI for better user experience.
- Easily extendable for new input fields or styling.
 
