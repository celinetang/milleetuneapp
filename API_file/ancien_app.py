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
        "name": "Display_picture",
        "description": "Display your picture !",
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

# class BlogArticles(BaseModel):
#     title: str
#     content: str
#     author: str = "Anonymous Author"

# class PredictionFeatures(BaseModel):
#     YearsExperience: float

# df = pd.read_excel("data/ibm_hr_attrition.xlsx")

@app.get("/preview",tags=["Insect_dataframe_preview"])
async def preview(rows: int=5):
    df = pd.read_csv("esoc_name_file.csv",encoding = 'unicode_escape')
    viz = df.head(rows)
    return viz.to_json()
# ici on pourrait aller chercher le dataset sur s3
# https://insects-s3.s3.eu-west-3.amazonaws.com/esoc_name_file.csv





# Load model
model = tf.keras.applications.inception_v3.InceptionV3(input_shape=(299, 299,3),
                                               include_top=False,
                                               weights = "imagenet"
                                               )









# @app.post("/display", tags=["Display_picture"])
# async def create_upload_file(file: UploadFile = File(...)):
#     # Save the uploaded file
#     contents = await file.read()
#     with open(file.filename, "wb") as f:
#         f.write(contents)
#     # Display the uploaded picture
#     image = Image.open(file.filename)
#     image.show()
#     return {"filename": file.filename}



@app.post("/upload", tags=["Upload_file"])
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}


# Define the upload directory
UPLOAD_DIR = "/app/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/predict", tags=["Predict_the_insect_common_name"])
async def predict(file: UploadFile = File(...)):
    # Save the uploaded image to the upload directory
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    # ca crée un path pour save l'image dans le docker
    with open(file_path, "wb") as buffer:
        # ca ouvre le path en question en "write-binary mode"
        # et prépare un file buffer qui va contenir les infos de l'image
        buffer.write(await file.read())
        # await file.read lit le fichier uploadé
        # buffer.write écrit ce qu'il lit dans le fichier buffer

        # ON DOIT AJOUTER UN PREPROCESS ICI !!!!!!

        predictions = model.predict(file.file)
        # Prepare the response
        response = {
        "predictions": predictions.tolist()
        }
        # Return the response
        return response

# def preprocess_image(image):
#     # Preprocess the image
#     # ...
#     return processed_image






# @app.post("/predict")
# async def predict(predictionFeatures: PredictionFeatures):
#     """
#     Prediction of salary for a given year of experience! 
#     """
#     # Read data 
#     years_experience = pd.DataFrame({"YearsExperience": [predictionFeatures.YearsExperience]})

#     # Log model from mlflow 
#     logged_model = 'runs:/3392c66a0fc1486bba1eea4c73d6ab05/salary_estimator'

#     # Load model as a PyFuncModel.
#     loaded_model = mlflow.pyfunc.load_model(logged_model)

#     # If you want to load model persisted locally
#     #loaded_model = joblib.load('salary_predictor/model.joblib')

#     prediction = loaded_model.predict(years_experience)

#     # Format response
#     response = {"prediction": prediction.tolist()[0]}
#     return response




# model_test = tf.keras.Sequential([
#     hub.KerasLayer("https://tfhub.dev/google/imagenet/mobilenet_v1_100_224/classification/5%22")
# ])
# model_test.build([None, 224, 224, 3])  # Batch input shape.

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=4000)