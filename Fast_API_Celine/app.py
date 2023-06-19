import uvicorn
import pandas as pd 
from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile
import mlflow
from PIL import Image
import numpy as np
import tensorflow as tf
import os
from sklearn.datasets import load_iris
import boto3




### 
# Here you can define some configurations 
###

app = FastAPI()

def get_img_array(img, size):
    # `img` is a PIL image of size 299x299
    # img = tf.keras.preprocessing.image.load_img(img_path, target_size=size)
    array = tf.image.resize(img,size)
    # `array` is a float32 Numpy array of shape (299, 299, 3)
    # array = tf.keras.preprocessing.image.img_to_array(img)
    # normalize array
    array = array / 255.0
    # We add a dimension to transform our array into a "batch"
    # of size (1, 299, 299, 3)
    array = np.expand_dims(array, axis=0)
    return array


@app.get("/hello")
async def index():
    return "hello"



@app.post("/predict", tags=["Machine Learning"])
# async def predict(file: UploadFile = File(...)):
async def create_upload_file(file: UploadFile):    
    #  or try to preprocess_image with contents
    # https://stackoverflow.com/questions/66162654/fastapi-image-post-and-resize
    # contents = await file.read()
    
    # Read data 
    img = Image.open(file.file)
    img_array = np.array(img)
    preprocessed_image = get_img_array(img_array,(299,299))
        

    # Log model from mlflow 
    logged_model = 's3://butterfly-s3-bucket/6/8dd0620ab01d4f6e9ec104e5dfd730c6/artifacts/model'

    # Load model as a PyFuncModel.
    loaded_model = mlflow.pyfunc.load_model(logged_model)

    # Predict on a np array
    preds = loaded_model.predict(preprocessed_image)
    pred_labels = tf.argmax(preds, axis = -1)

#     class_labels = df.labels.unique().tolist()
# # Get the predicted label index
#     pred_label_index = tf.argmax(preds, axis=-1).numpy()[0]
# # Get the predicted class name
#     predicted_class = class_labels[pred_label_index]
    
#     print("Predicted class:", predicted_class)
    #Format response
    response = {"prediction": pred_labels.tolist()[0]}
    return response


if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=4000) # Here you define your web server to run the `app` variable (which contains FastAPI instance), with a specific host IP (0.0.0.0) and port (4000)


