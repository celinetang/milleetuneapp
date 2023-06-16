import uvicorn
import pandas as pd 
from pydantic import BaseModel
from typing import Literal, List, Union
from fastapi import FastAPI, File, UploadFile
import joblib
import tensorflow as tf
import mlflow
import os
from PIL import Image
import numpy as np
from tensorflow.keras.applications.inception_v3 import decode_predictions

description = """
API pour le pont entre notre page streamlit (front end) et nos modèles
"""

tags_metadata = [
    {
        "name": "Insect_dataframe_preview",
        "description": "Preview of a number of your choice of samples from the dataset",
    },
    {
        "name": "Upload_file",
        "description": "Upload and preview your insect picture",
    },
    {
        "name": "Predict_the_insect_common_name",
        "description": "Predict the insect common name"
    }
]


app = FastAPI(
    # title="🪐 1001 APP",
    # description=description,
    # version="0.1",
    # contact={
    #     "name": "Jedha",
    #     "url": "https://jedha.co",
    # },
    # openapi_tags=tags_metadata
)


@app.get("/preview",tags=["Insect_dataframe_preview"])
async def preview(rows: int=5):
    df = pd.read_csv("esoc_name_file.csv",encoding = 'unicode_escape')
    viz = df.head(rows)
    return viz.to_json()
# ici on pourrait aller chercher le dataset sur s3
# https://insects-s3.s3.eu-west-3.amazonaws.com/esoc_name_file.csv


@app.post("/upload", tags=["Upload_file"])
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}


"""""""""""""""""""""""""""""""""""""""""   Load model   """""""""""""""""""""""""""""""""""""""""

def load_model():
    model = tf.keras.applications.inception_v3.InceptionV3(input_shape=(299, 299,3),
                                               include_top=False,
                                               weights = "imagenet")
    print("Model loaded")
    return model

model = load_model()

# Check model summary
print(model.summary())
# Check model input and output shapes
print("Input shape:", model.input_shape)
print("Output shape:", model.output_shape)
# Verify model weights are loaded
print("Model weights loaded:", len(model.weights) > 0)

"""""""""""""""""""""""""""""""""""""""""   Process picture   """""""""""""""""""""""""""""""""""""""""

def preprocess_image(image):
    resized_image = tf.image.resize(image,(299, 299))
    normalized_image = (resized_image / 255.0 - 0.5) * 2.0
    preprocessed_image = tf.expand_dims(normalized_image, axis=0)
    return preprocessed_image

"""""""""""""""""""""""""""""""""""""""""   Prediction  """""""""""""""""""""""""""""""""""""""""

import logging
import traceback

@app.post("/predict", tags=["Predict_the_insect_common_name"])
async def predict(file: UploadFile = File(...)):
    try:
        image = Image.open(file.file)
        preprocessed_image = preprocess_image(image)
        predictions = model.predict(preprocessed_image)
        decoded_predictions = decode_predictions(predictions,top=3)
        response = {
            "predictions": decoded_predictions.tolist()
        }
        # Print the response for inspection
        print(response)
        # Return the response
        return response
    except Exception as e:
        # Log the exception
        logging.exception("An error occurred during prediction:")
        traceback.print_exc()
        # Return an error response
        return {"error": "An error occurred during prediction."}


if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=4000)




    # @app.post("/predict", tags=["Predict_the_insect_common_name"])
# async def predict(file: UploadFile = File(...)):
#     image = Image.open(file.file)
#     preprocessed_image = preprocess_image(image)
#     predictions = model.predict(preprocessed_image)
#     response = {
#     "predictions": predictions.tolist()
#     }
#     print(response)
#     # Return the response
#     return response