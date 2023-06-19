import uvicorn
import pandas as pd 
from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile
import mlflow
from PIL import Image
import numpy as np
import os
import boto3


### 
# Here you can define some configurations 
###

app = FastAPI()


@app.get("/hello")
async def index():
    return "hello"

class PredictionFeatures(BaseModel):
    YearsExperience: float

@app.post("/predict", tags=["Machine Learning"])
async def predict(predictionFeatures: PredictionFeatures):
    """
    Prediction of salary for a given year of experience! 
    """
    # Read data 
    years_experience = pd.DataFrame({"YearsExperience": [predictionFeatures.YearsExperience]})

    # Log model from mlflow 
    logged_model = 's3://butterfly-s3-bucket/9/405ede28de6f43ffbabf45f0a315e1d8/artifacts/model'

    # Load model as a PyFuncModel.
    loaded_model = mlflow.pyfunc.load_model(logged_model)
    prediction = loaded_model.predict(years_experience)

    # Format response
    response = {"prediction": prediction.tolist()[0]}
    return response

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=4000) # Here you define your web server to run the `app` variable (which contains FastAPI instance), with a specific host IP (0.0.0.0) and port (4000)


