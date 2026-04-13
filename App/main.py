import pandas as pd
import pickle
from fastapi import FastAPI
from App.schema import InputData

app = FastAPI(title="Depression Model")

# Load model
model = pickle.load(open("model/model.pkl", "rb"))

# Load feature columns
feature_columns = pickle.load(open("model/features.pkl", "rb"))

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/predict")
def predict(data: InputData):

    # Convert input to DataFrame
    input_dict = data.dict()
    input_df = pd.DataFrame([input_dict])

    # One-hot encode (same as training)
    input_df = pd.get_dummies(input_df)

    # Align columns with training data
    input_df = input_df.reindex(columns=feature_columns, fill_value=0)

    # Predict
    prediction = model.predict(input_df)[0]

    return {
        "prediction": int(prediction)
    }