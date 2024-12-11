# Mille et Une App

**Mille et Une App** is a collaborative project by Zouhair, Céline, and Élo, aimed at developing a system for recognizing butterflies. The application integrates machine learning algorithms with FastAPI and Streamlit to provide an interactive platform for insect identification.

## Deliverables

**Check out our app here : 👉 [go to app](https://papillon-streamlit-bfb375963555.herokuapp.com/)**

DemoDay video presentation (watch group 1 from 6'40 to 19'): [watch here](https://www.youtube.com/watch?v=5qngzP4DGGU )

Personal video presentation : https://share.vidyard.com/watch/rXKxxcsA8ttzJoaiwSYCc4?

Powerpoint presentation : [here](https://docs.google.com/presentation/d/1iaaTtyrFAPNk3UaQ-5sxpDKRRIIILs7gO6IsiAauOXQ/edit#slide=id.ga5178bf3d4_2_0)

## Project Overview

The Mille et Une App' is an online app that helps you identify the butterfly you see. Take a picture of the butterfly, upload it, and the app will try its best to recognize it and suggest it's name, and give out main information about the species.

An additional feature with geolocalisation is added to help entomologist track down the butterfly biosphere.

## Features

- **Insect Identification**: Utilizes machine learning models to accurately classify various butterfly species.
- **API Integration**: Employs FastAPI to handle backend processes and API endpoints.
- **User Interface**: Implements Streamlit for a user-friendly frontend experience.
- **Model Tracking**: Incorporates MLflow for tracking and managing machine learning experiments.


## Objective
Different tools were used to create the system's interacting with each other

- Dataset from Kaggle containing : 100 butterfly or moth species
    - 12594 images in train set, 500 test, 500 validation images 224 X 224 X 3 jpg format 
    - https://www.kaggle.com/datasets/gpiosenka/butterfly-images40-species
- Set up monitoring various Machine Learning models via MLFlow
    - https://butterfly-mlflow-8cf571945f28.herokuapp.com/
    - MLFlow source code in 1_MLFlow/
    - Note : muliple machine learning models have been done during project, however, the original MLFlow set up was deleted (for cost reasons). This is why this one seems quite empty, but is hown here to see its functioning
- Train a model via Kaggle notebook Inception V3 model : 
    - Model source code in: 2_ML/papillon-100cat-10epoch.ipynb
    - model.h5 files are not pushed on Github as too heavy -
- Load the model on FastAPI deployed with Heroku : 
    - https://papillon-api-1e396125389e.herokuapp.com/docs
    - Source code in: 3_FastAPI/app.py
- Online app interface created with Stremlit deployed with Heroku : 
    - https://papillon-streamlit-bfb375963555.herokuapp.com/
    - Source code in: 4_Streamlit/app.py
 
## Tech Stack

- **Backend**: FastAPI
- **Frontend**: Streamlit
- **Machine Learning**: Jupyter Notebook, MLflow
- **Programming Languages**: Python
- **Containerization**: Docker

## Usage

1. **Upload an Image**:
   - Access the Streamlit interface to upload a butterfly image.

2. **View Prediction**:
   - The machine learning model processes the image and displays the predicted species along with confidence scores.

3. **Explore Results**:
   - Utilize the interactive dashboard to analyze predictions and related information.



## Getting Started

To set up the project locally, follow these steps:

### Prerequisites

- Python 3.8+
- Docker
- Virtual environment tool (e.g., `venv` or `conda`)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/celinetang/milleetuneapp.git
   cd milleetuneapp
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   - Create a `.env` file in the project root.
   - Add the necessary environment variables:
     ```env
     DATABASE_URL=your-database-url
     FASTAPI_PORT=8000
     STREAMLIT_PORT=8501
     SECRET_KEY=your-secret-key
     ```

5. **Run the FastAPI backend**:
   ```bash
   uvicorn API_file.main:app --reload --port 8000
   ```

6. **Run the Streamlit frontend**:
   ```bash
   streamlit run Streamlit_file/app.py --server.port 8501
   ```

## Project Structure

```
milleetuneapp/
│
├── API_file/
│   ├── main.py               # FastAPI application entry point
│   └── ...                   # Additional API modules
│
├── Models/
│   ├── model.py              # Machine learning model definition
│   └── ...                   # Additional model-related files
│
├── Streamlit_file/
│   ├── app.py                # Streamlit application entry point
│   └── ...                   # Additional frontend components
│
├── Mlflow/
│   ├── tracking.py           # MLflow tracking scripts
│   └── ...                   # Additional MLflow configurations
│
├── data/                     # Dataset for training and testing
├── requirements.txt          # Python dependencies
├── Dockerfile                # Docker configuration
└── README.md                 # Project documentation
```


## Prerequisites

- The source code is written in Python 3.
- To locally run app and API you need Docker and Heroku 

## Team contributors
Elodie Sune<br/>
Céline Tang<br/>
Zouhair Khomsi<br/>
