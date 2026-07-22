<div align="center">

# 🎓 Student Performance Indicator

### End-to-End Machine Learning Regression Project using Streamlit

Predict a student's **Math Score** based on demographic and academic factors using Machine Learning.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge&logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-black?style=for-the-badge&logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical_Computing-blue?style=for-the-badge&logo=numpy)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

# 📌 Overview

Student academic performance depends on several factors beyond intelligence alone. Variables such as **gender, ethnicity, parental education level, lunch type, and test preparation** can significantly influence examination scores.

This project is an **End-to-End Machine Learning Regression application** that predicts a student's **Math Score** using these features.

The project demonstrates the complete Machine Learning workflow:

- Data Analysis
- Data Preprocessing
- Feature Engineering
- Model Training
- Model Evaluation
- Model Selection
- Model Serialization
- Streamlit Web Application
- Deployment Ready Structure

---

# 🚀 Features

✅ End-to-End Machine Learning Pipeline

✅ Data Cleaning & Preprocessing

✅ Multiple Regression Algorithms Comparison

✅ Best Model Selection

✅ Model Serialization using Pickle

✅ Interactive Streamlit Web Interface

✅ Predict Student Math Score Instantly

✅ Modular Project Structure

---

# 🎯 Problem Statement

The objective of this project is to predict a student's **Math Score** using the following information:

- Gender
- Race / Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score

The trained model estimates the expected Math Score for a student based on these features.

---

# 🧠 Machine Learning Workflow

```text
Dataset
    │
    ▼
Data Preprocessing
    │
    ▼
Feature Engineering
    │
    ▼
Train-Test Split
    │
    ▼
Train Multiple Regression Models
    │
    ▼
Evaluate Models
    │
    ▼
Select Best Performing Model
    │
    ▼
Save Model
    │
    ▼
Streamlit Web Application
```

---

# 📊 Regression Algorithms Used

Multiple Machine Learning regression algorithms were trained and evaluated to identify the best-performing model.

The project includes models such as:

- Linear Regression
- Lasso Regression
- Ridge Regression
- K-Nearest Neighbors Regressor
- Decision Tree Regressor
- Random Forest Regressor
- AdaBoost Regressor
- Gradient Boosting Regressor
- XGBoost Regressor
- CatBoost Regressor

The model with the highest evaluation score was selected for prediction.

---

# 📁 Project Structure

```text
Student_Performance_Indicator/
│
├── artifacts/
│   ├── model.pkl
│   ├── preprocessor.pkl
│
├── notebook/
│   ├── EDA.ipynb
│   ├── Model Training.ipynb
│
├── Screenshot/
│   ├── Home.png
│   ├── Prediction.png
│
├── src/
│   ├── components/
│   │      ├── data_ingestion.py
│   │      ├── data_transformation.py
│   │      └── model_trainer.py
│   │
│   ├── pipeline/
│   │      ├── predict_pipeline.py
│   │      └── train_pipeline.py
│   │
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── app.py
├── requirements.txt
├── setup.py
└── README.md
```

---

# 📂 Dataset Features

| Feature | Description |
|----------|-------------|
| Gender | Male / Female |
| Race/Ethnicity | Student ethnic group |
| Parental Education | Highest education level of parents |
| Lunch | Standard / Free or Reduced |
| Test Preparation Course | Completed / None |
| Reading Score | Reading examination marks |
| Writing Score | Writing examination marks |

### 🎯 Target Variable

```
Math Score
```

---

# 📈 Model Evaluation

Several regression algorithms were trained and compared using regression evaluation metrics.

Evaluation Metrics include:

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

The best-performing model was selected for deployment.

---

# 💻 Streamlit Web Application

The project includes an interactive **Streamlit application** where users can:

- Enter student details
- Submit the form
- Instantly predict Math Score

---

# 📸 Application Screenshots

## Home Page

<p align="center">
<img src="Screenshot/Home.png" width="900">
</p>

---

## Prediction Page

<p align="center">
<img src="Screenshot/Prediction.png" width="900">
</p>

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/aniruddha-alkari/Student_Performance_Indicator.git
```

Move into project directory

```bash
cd Student_Performance_Indicator
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

Launch the Streamlit application

```bash
streamlit run app.py
```

After launching, open your browser and visit

```
http://localhost:8501
```

---

# 🧪 Example Prediction

### Input

| Feature | Value |
|---------|-------|
| Gender | Female |
| Race | Group C |
| Parental Education | Bachelor's Degree |
| Lunch | Standard |
| Test Preparation | Completed |
| Reading Score | 75 |
| Writing Score | 80 |

### Output

```
Predicted Math Score

≈ 78
```

---

# 🛠️ Technologies Used

### Programming

- Python

### Machine Learning

- Scikit-learn
- XGBoost
- CatBoost

### Data Analysis

- Pandas
- NumPy

### Visualization

- Matplotlib
- Seaborn

### Frontend

- Streamlit

### Model Serialization

- Pickle

---

# ⭐ Key Learning Outcomes

This project demonstrates:

- End-to-End Machine Learning Pipeline
- Feature Engineering
- Regression Algorithms
- Model Evaluation
- Pipeline Creation
- Object-Oriented Programming
- Exception Handling
- Logging
- Modular Code Architecture
- Streamlit Deployment

---

# 🔮 Future Improvements

- Deploy on Streamlit Cloud
- Docker Support
- CI/CD Pipeline
- Model Monitoring
- Explainable AI using SHAP
- Hyperparameter Optimization
- MLflow Experiment Tracking

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Aniruddha Alkari**

GitHub:

https://github.com/aniruddha-alkari

---

<div align="center">

### ⭐ If you found this project useful, don't forget to Star the repository!

</div>