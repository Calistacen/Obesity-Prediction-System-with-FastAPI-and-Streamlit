# As usual import
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import PreProcessorNew_pipeline
import logging


# Load model
with open("ObessityRF.pkl", "rb") as f:
    model = pickle.load(f)

# Reverse mapping for prediction output
reverse_mapping = {
    0: 'Insufficient_Weight',
    1: 'Normal_Weight',
    2: 'Overweight_Level_I',
    3: 'Overweight_Level_II',
    4: 'Obesity_Type_I',
    5: 'Obesity_Type_II',
    6: 'Obesity_Type_III'
}

# Define input schema
class UserInput(BaseModel):
    Gender: str #mostlikely radio input
    Age: float #numerical input
    Height: float #numerical input
    Weight: float #numerical input
    NCP: float #likert input
    CAEC: str #radio input
    FCVC: float #likert input
    CH2O: float #liker input 
    FAF: float #likert input
    TUE: float #liekrt input
    

# Callin those API
app = FastAPI()

@app.post("/predict")
def predict(data: UserInput):
    input_dict = data.dict()
    logging.info(f"Received input: {input_dict}")

    # Add logging just in case error happen so we know where to handle 
    try:
        input_df = pd.DataFrame([input_dict])
        prediction = model.predict(input_df)[0]
        result = reverse_mapping[prediction]
        logging.info(f"Prediction: {result}")
        return {"prediction": result}
    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        return {"error": "Prediction failed"}

# Ready to deploy