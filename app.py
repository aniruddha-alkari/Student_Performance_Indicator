import streamlit as st

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# ---------------------------------------
# Page Title
# ---------------------------------------
st.title("🎓 Student Performance Predictor")

st.write("Enter student details and click Predict.")

# ---------------------------------------
# Input Fields
# ---------------------------------------

gender = st.selectbox(
    "Gender",
    ["male", "female"]
)

ethnicity = st.selectbox(
    "Race / Ethnicity",
    [
        "group A",
        "group B",
        "group C",
        "group D",
        "group E"
    ]
)

parental_level_of_education = st.selectbox(
    "Parental Education",
    [
        "associate's degree",
        "bachelor's degree",
        "high school",
        "master's degree",
        "some college",
        "some high school"
    ]
)

lunch = st.selectbox(
    "Lunch",
    [
        "free/reduced",
        "standard"
    ]
)

test_preparation_course = st.selectbox(
    "Test Preparation Course",
    [
        "completed",
        "none"
    ]
)

reading_score = st.number_input(
    "Reading Score",
    min_value=0,
    max_value=100,
    value=50
)

writing_score = st.number_input(
    "Writing Score",
    min_value=0,
    max_value=100,
    value=50
)

# ---------------------------------------
# Predict Button
# ---------------------------------------

if st.button("Predict Maths Score"):

    data = CustomData(
        gender=gender,
        race_ethnicity=ethnicity,
        parental_level_of_education=parental_level_of_education,
        lunch=lunch,
        test_preparation_course=test_preparation_course,
        reading_score=reading_score,
        writing_score=writing_score
    )

    pred_df = data.get_data_as_data_frame()

    pipeline = PredictPipeline()

    result = pipeline.predict(pred_df)

    st.success(f"Predicted Maths Score : {result[0]:.2f}")