import streamlit as st
import pandas as pd
import numpy as np

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Set page configuration
st.set_page_config(
    page_title="Student Performance Indicator",
    page_icon="🎓",
    layout="centered"
)

# App title and description
st.title("🎓 Student Performance Indicator")
st.markdown("""
This web application predicts a student's **Math Score** based on demographic and academic performance metrics. 
Fill in the details below and click **Predict** to see the results.
""")

# Form container for a clean UI layout
st.subheader("Enter Student Details")

with st.form("prediction_form"):
    # Group inputs into columns for better visual organization
    col1, col2 = st.columns(2)
    
    with col1:
        gender = st.selectbox(
            "Gender", 
            options=["female", "male"]
        )
        
        race_ethnicity = st.selectbox(
            "Race/Ethnicity Group", 
            options=["group A", "group B", "group C", "group D", "group E"]
        )
        
        parental_level_of_education = st.selectbox(
            "Parental Level of Education", 
            options=[
                "some high school", 
                "high school", 
                "associate's degree", 
                "some college", 
                "bachelor's degree", 
                "master's degree"
            ]
        )
        
    with col2:
        lunch = st.selectbox(
            "Lunch Type", 
            options=["standard", "free/reduced"]
        )
        
        test_preparation_course = st.selectbox(
            "Test Preparation Course", 
            options=["none", "completed"]
        )
        
        reading_score = st.number_input(
            "Reading Score (0 - 100)", 
            min_value=0, 
            max_value=100, 
            value=70, 
            step=1
        )
        
        writing_score = st.number_input(
            "Writing Score (0 - 100)", 
            min_value=0, 
            max_value=100, 
            value=70, 
            step=1
        )
    
    # Form submission button
    submit_button = st.form_submit_button(label="Predict Math Score")

# Logic to run when the user clicks 'Predict Math Score'
if submit_button:
    try:
        # Initialize the CustomData class with the user inputs
        data = CustomData(
            gender=gender,
            race_ethnicity=race_ethnicity,
            parental_level_of_education=parental_level_of_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            reading_score=int(reading_score),
            writing_score=int(writing_score)
        )
        
        # Convert input data into a pandas DataFrame format expected by the pipeline
        pred_df = data.get_data_as_data_frame()
        
        # Initialize the prediction pipeline and fetch prediction
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        
        # Display success message with the formatted result
        predicted_score = round(results[0], 2)
        st.success(f"### 🎯 Predicted Math Score: **{predicted_score}**")
        
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")