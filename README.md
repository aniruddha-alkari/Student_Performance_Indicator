# 🎓 Student Performance Indicator

An End-to-End Machine Learning Project that predicts student mathematics performance based on demographic, educational, and socio-economic factors.

The project covers the complete Machine Learning lifecycle including data ingestion, data preprocessing, model training, model evaluation, and a user-friendly web application built using Streamlit.

---

## 🚀 Project Overview

Educational institutions generate large amounts of student data. Analyzing this data can help identify factors that influence academic performance.

This project predicts a student's **Math Score** using various attributes such as:

* Gender
* Race/Ethnicity
* Parental Level of Education
* Lunch Type
* Test Preparation Course
* Reading Score
* Writing Score

The application allows users to enter student information through a web interface and instantly receive a predicted math score.

---

## 📌 Problem Statement

The objective of this project is to understand how different factors affect student academic performance and build a machine learning model capable of accurately predicting student math scores.

---

## 📊 Dataset Information

Dataset Source:

https://www.kaggle.com/datasets/spscientist/students-performance-in-exams

### Features

| Feature                     | Description                      |
| --------------------------- | -------------------------------- |
| Gender                      | Male / Female                    |
| Race/Ethnicity              | Group A-E                        |
| Parental Level of Education | Parent's highest education level |
| Lunch                       | Standard / Free-Reduced          |
| Test Preparation Course     | Completed / Not Completed        |
| Reading Score               | Reading exam score               |
| Writing Score               | Writing exam score               |

### Target Variable

**Math Score**

---

## 🏗️ Project Architecture

```text
Student_Performance_Indicator
│
├── artifacts/
│   ├── model.pkl
│   ├── preprocessor.pkl
│
├── notebook/
│   ├── EDA.ipynb
│   ├── Model_Training.ipynb
│
├── src/
│   ├── components/
│   ├── pipeline/
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── Screenshot/
│
├── app.py
├── requirements.txt
├── setup.py
└── README.md
```

---

## ⚙️ Machine Learning Pipeline

### 1️⃣ Data Ingestion

* Reads raw dataset
* Splits data into train and test sets
* Stores processed datasets

### 2️⃣ Data Transformation

* Missing value handling
* Feature engineering
* Categorical encoding
* Feature scaling
* Pipeline creation using Scikit-Learn

### 3️⃣ Model Training

Multiple regression algorithms are trained and evaluated:

* Linear Regression
* Ridge Regression
* Lasso Regression
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor
* XGBoost Regressor
* CatBoost Regressor
* AdaBoost Regressor

### 4️⃣ Model Evaluation

Models are compared using:

* R² Score
* MAE
* MSE
* RMSE

### 5️⃣ Prediction Pipeline

* Loads trained model
* Applies preprocessing pipeline
* Generates final prediction

### 6️⃣ Streamlit Web Application

Interactive user interface allowing users to:

* Enter student details
* Predict math score instantly
* View results in browser

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-Learn
* XGBoost
* CatBoost

### Web Framework

* Streamlit

### Version Control

* Git
* GitHub

---

## 📷 Application Screenshots

![App Screenshot](screenshots\Screenshot 2026-06-24 130323.png)


![alt text](screenshots\Screenshot 2026-06-24 130522.png)


---

## 🔧 Installation & Setup

### Clone Repository

```bash
git clone https://github.com/aniruddha-alkari/Student_Performance_Indicator.git
```

### Navigate to Project

```bash
cd Student_Performance_Indicator
```

### Create Virtual Environment

```bash
conda create -p venv python=3.8 -y
```

### Activate Environment

```bash
conda activate venv/
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 📈 Model Workflow

```text
Raw Data
   │
   ▼
Data Ingestion
   │
   ▼
Data Validation
   │
   ▼
Data Transformation
   │
   ▼
Model Training
   │
   ▼
Model Evaluation
   │
   ▼
Model Selection
   │
   ▼
Prediction Pipeline
   │
   ▼
Streamlit Application
```

---

## 🌟 Key Features

✅ End-to-End Machine Learning Pipeline

✅ Modular Project Structure

✅ Object-Oriented Design

✅ Custom Exception Handling

✅ Logging System

✅ Automated Data Processing

✅ Multiple Model Comparison

✅ Streamlit Web Application

✅ Cloud Deployment Ready

---

## 📚 Learning Outcomes

This project demonstrates:

* Machine Learning Project Lifecycle
* Data Preprocessing Techniques
* Feature Engineering
* Model Selection & Evaluation
* Production-Level Project Structure
* Streamlit Application
* MLOps Fundamentals

---

## 👨‍💻 Author

### Aniruddha Alkari

Machine Learning Engineer | Python Developer | AI Enthusiast

* GitHub: https://github.com/aniruddha-alkari
* LinkedIn: https://www.linkedin.com/in/anialkari96/

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future improvements.
