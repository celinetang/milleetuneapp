import uvicorn
import pandas as pd 
from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile
import mlflow
from PIL import Image
import numpy as np
import tensorflow as tf



### 
# Here you can define some configurations 
###

app = FastAPI()

def preprocess_image(image):
    resized_image = tf.image.resize(image,(299, 299))
    normalized_image = (resized_image / 255.0 - 0.5) * 2.0
    preprocessed_image = tf.expand_dims(normalized_image, axis=0)
    return preprocessed_image

@app.get("/hello")
async def index():
    return "hello"


@app.post("/predict", tags=["Machine Learning"])
async def predict(file: UploadFile = File(...)):
    
    #  or try to preprocess_image with contents
    # https://stackoverflow.com/questions/66162654/fastapi-image-post-and-resize
    # contents = await file.read()
    
    # Read data 
    img = Image.open(file)
    preprocessed_image = preprocess_image(img)
        

    # Log model from mlflow 
    logged_model = 'runs:/e0130093eadd49789c76e7b9b2b7cd39/model'

    # Load model as a PyFuncModel.
    loaded_model = mlflow.pyfunc.load_model(logged_model)

    # Predict on a np array
    prediction = loaded_model.predict(preprocessed_image)

    #Format response
    response = {"prediction": np.argmax(prediction), "confidence": prediction[0][np.argmax(prediction)]}
    return response
  






if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=4000) # Here you define your web server to run the `app` variable (which contains FastAPI instance), with a specific host IP (0.0.0.0) and port (4000)


