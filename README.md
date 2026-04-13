# Machine Learning Pipeline with FastAPI Deployment

## Project Overview
This project demonstrates a complete end-to-end machine learning workflow, including data preprocessing, model training, evaluation, and deployment as a REST API using FastAPI. The model is trained using scikit-learn and serves real-time predictions through a web interface.

---

## Objective
To build a simple and functional machine learning system that:
- Processes and prepares data for modeling
- Trains a predictive model using a public dataset
- Evaluates model performance
- Deploys the trained model as an API for real-time inference
- Provides a basic framework for monitoring model performance in production

---

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- FastAPI
- Uvicorn
- Pickle (model serialization)

---



## Workflow

### 1. Data Preprocessing
- Handled missing values (if any)
- Converted categorical variables using one-hot encoding
- Ensured feature consistency between training and inference

### 2. Model Training
- Split dataset into training and testing sets
- Trained a supervised machine learning model using scikit-learn
- Evaluated performance using standard metrics

### 3. Model Serialization
- Saved trained model using Pickle
- Stored feature columns to ensure consistency during inference

### 4. API Deployment
- Built a REST API using FastAPI
- Created a `/predict` endpoint to receive input data
- Returned real-time predictions from the trained model


