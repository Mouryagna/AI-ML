from fastapi import FastAPI
from fastapi.responses import JSONResponse
from model.predict import predict_output,model,MODEL_VERSION
from schema.prediction_response import PredictionResponse

from schema.user_input import UserInput
import pickle


#import model pickle
with open('model/model.pkl', 'rb') as f:
    model=pickle.load(f)

MODEL_VERSION="1.0.0"

app=FastAPI()

@app.get('/')
def home():
    return {"message":"Insurance Premium Prediction API"}

#machine readable ***
@app.get('/health')
def health_check():
    return {
        "status":"ok",
        "version":MODEL_VERSION,
        "model_loaded": model is not None
    }

@app.post('/predict',response_model=PredictionResponse)
def predict_premium(data:UserInput):

    user_input={
        'bmi':data.bmi,
        'age_group':data.age_group,
        'lifestyle_risk':data.lifestyle_risk,
        'city_tier':data.city_tier,
        'income_lpa':data.income_lpa,
        'occupation':data.occupation
    }
    try:
        predict=predict_output(user_input)
        return JSONResponse(status_code=200,content={'predicted_category':predict})

    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))