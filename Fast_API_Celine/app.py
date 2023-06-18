import uvicorn
import pandas as pd 
from pydantic import BaseModel
from typing import Literal, List, Union
from fastapi import FastAPI, File, UploadFile
# import joblib
# import tensorflow as tf
# import mlflow
# import os
# from PIL import Image
# import numpy as np



### 
# Here you can define some configurations 
###

app = FastAPI()

@app.get("/hello")
async def index():
    return "hello"

"""
@app.post("/upload", tags=["Upload_file"])
async def create_upload_file(file: UploadFile = File(...)):
  return {"filename": file.filename}

 

logged_model = 'runs:/e0130093eadd49789c76e7b9b2b7cd39/model'
@app.post("/predict", tags=["Machine Learning"])
async def predict(file : UploadFile = File(...)):
    """
    #Prediction of butterfly category
    """
    # Read data 
    input_photo = Image.open(file.file)

    # Log model from mlflow 
    logged_model = 'runs:/323c3b4a6a6242b7837681bd5c539b27/salary_estimator'

    # Load model as a PyFuncModel.
    loaded_model = mlflow.pyfunc.load_model(logged_model)
    prediction = loaded_model.predict(input_photo)
    # Format response
    response = {"prediction": prediction.tolist()[0]}
    return response

"""


if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=4000) # Here you define your web server to run the `app` variable (which contains FastAPI instance), with a specific host IP (0.0.0.0) and port (4000)


