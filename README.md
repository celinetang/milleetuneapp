# Mille et Une App

**Mille et Une App** is a collaborative project by Zouhair, Céline, and Élo, aimed at developing a system for recognizing butterflies. The application integrates machine learning algorithms with FastAPI and Streamlit to provide an interactive platform for insect identification.

## Features

- **Insect Identification**: Utilizes machine learning models to accurately classify various butterfly species.
- **API Integration**: Employs FastAPI to handle backend processes and API endpoints.
- **User Interface**: Implements Streamlit for a user-friendly frontend experience.
- **Model Tracking**: Incorporates MLflow for tracking and managing machine learning experiments.

## Tech Stack

- **Backend**: FastAPI
- **Frontend**: Streamlit
- **Machine Learning**: Jupyter Notebook, MLflow
- **Programming Languages**: Python
- **Containerization**: Docker

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

## Usage

1. **Upload an Image**:
   - Access the Streamlit interface to upload a butterfly image.

2. **View Prediction**:
   - The machine learning model processes the image and displays the predicted species along with confidence scores.

3. **Explore Results**:
   - Utilize the interactive dashboard to analyze predictions and related information.

## Contributing

Contributions are welcome! To contribute:

1. **Fork the repository**.
2. **Create a new branch**:
   ```bash
   git checkout -b feature/your-feature
   ```
3. **Commit your changes**:
   ```bash
   git commit -m "Description of your feature"
   ```
4. **Push to your branch**:
   ```bash
   git push origin feature/your-feature
   ```
5. **Submit a pull request**.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, please open an issue in the repository.

---

This README provides an overview of the Mille et Une App project, including setup instructions and contribution guidelines. 
