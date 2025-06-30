# 🪴 IRIS-MLOPS-PIPELINE

An end-to-end **MLOps pipeline** for training, deploying, and serving an Iris flower classification model using **Docker**, **GitHub Actions**, and **Google Cloud Platform Kubernetes Engine (GKE)**.

---

## 📂 Project Structure

```
sami-codeai-iris-mlops-pipeline/
├── README.md                  # Project documentation
├── application.py             # Flask app for model serving
├── Dockerfile                 # Docker image configuration
├── kubernetes-deployment.yaml # Kubernetes deployment specification
├── requirements.txt           # Python dependencies
├── setup.py                   # Setup script (optional)
├── artifacts/                 # Data & trained model artifacts
│   ├── models/
│   │   └── model.pkl          # Trained ML model
│   ├── processed/             # Processed training/testing data
│   └── raw/
│       └── data.csv           # Raw Iris dataset
├── notebook/
│   └── iris.ipynb             # Jupyter notebook for EDA & prototyping
├── pipeline/
│   ├── __init__.py
│   └── training_pipeline.py   # Training pipeline code
├── src/
│   ├── __init__.py
│   ├── custom_exception.py    # Custom exception handling
│   ├── data_processing.py     # Data preprocessing scripts
│   ├── logger.py              # Logging utility
│   └── model_training.py      # Model training logic
├── static/
│   └── style.css              # Stylesheet for the web app
├── templates/
│   └── index.html             # Frontend HTML template
└── .github/
    └── workflows/
        └── deploy.yml         # CI/CD workflow configuration
```

---

## 🌼 How It Works

**1️⃣ Data Processing**
The Iris dataset (`artifacts/raw/data.csv`) is preprocessed by `data_processing.py` to handle splitting into training and testing sets. The processed files are saved in `artifacts/processed/`.

**2️⃣ Model Training**
The `training_pipeline.py` uses the processed data to train a simple classification model (e.g., Logistic Regression, Decision Tree, etc.), which is saved as `model.pkl` in `artifacts/models/`.

**3️⃣ Model Serving**
The `application.py` is a Flask web app that loads `model.pkl` and provides an interface (via `index.html`) to input flower measurements and receive predictions.

**4️⃣ Containerization**
The application is containerized using the `Dockerfile`. It builds an image containing all necessary dependencies and exposes the Flask server.

**5️⃣ Deployment on GKE**
The `kubernetes-deployment.yaml` defines the Kubernetes Deployment and Service for deploying the containerized app on Google Kubernetes Engine (GKE).

---

## 🚀 CI/CD Workflow

The pipeline uses **GitHub Actions** for Continuous Integration and Continuous Deployment:

✅ **CI:**

* On every push or pull request:

  * Install dependencies (`requirements.txt`).
  * Run linting/tests (if added).
  * Build Docker image.
  * Run the container to check for runtime errors.

✅ **CD:**

* If the build succeeds on `main`:

  * Authenticate with Google Cloud.
  * Build and push the Docker image to Google Container Registry (GCR).
  * Deploy/update the image on Google Kubernetes Engine using `kubectl` with `kubernetes-deployment.yaml`.

The entire workflow is defined in `.github/workflows/deploy.yml`.

---

## 📌 How to Run Locally

1️⃣ **Clone the Repo**

```bash
git clone https://github.com/<your-username>/sami-codeai-iris-mlops-pipeline.git
cd sami-codeai-iris-mlops-pipeline
```

2️⃣ **Create Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3️⃣ **Install Dependencies**

```bash
pip install -r requirements.txt
```

4️⃣ **Run the Flask App**

```bash
python application.py
```

Visit `http://localhost:5000` in your browser.

---

## ☁️ Deploy to GKE

1️⃣ **Build Docker Image**

```bash
docker build -t iris-mlops-app .
```

2️⃣ **Push to Google Container Registry**

```bash
docker tag iris-mlops-app gcr.io/<your-project-id>/iris-mlops-app
docker push gcr.io/<your-project-id>/iris-mlops-app
```

3️⃣ **Deploy to Kubernetes**

```bash
kubectl apply -f kubernetes-deployment.yaml
kubectl get services
```


