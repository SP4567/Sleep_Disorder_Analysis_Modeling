import streamlit as st
import numpy as np
import tensorflow as tf

# Load the trained model
model_path = "sleep_model.h5"  # Replace with your model file path
model = tf.keras.models.load_model(model_path)

# Title and description
st.title("Sleep Disorder Prediction App")
st.write("""
This app predicts the likelihood of a sleep disorder based on user inputs. 
Fill in the details below to get the prediction.
""")

# Input fields
st.header("Input Features")
person_id = st.text_input("Person ID", "")
gender = st.number_input("Gender (0: Female, 1: Male)", min_value=0, max_value=1, step=1)
age = st.number_input("Age (years)", min_value=0, max_value=120, value=25, step=1)
occupation = st.number_input("Occupation (0-10)", min_value=0, max_value=10, value=0, step=1)
sleep_duration = st.slider("Sleep Duration (hours per night)", 0.0, 24.0, 7.0, 0.1)
quality_of_sleep = st.slider("Quality of Sleep", 1.0, 10.0, 7.0, 1.0)
physical_activity_level = st.slider("Physical Activity Level", 1.0, 10.0, 5.0, 1.0)
stress_level = st.slider("Stress Level", 1.0, 10.0, 5.0, 1.0)
bmi_category = st.number_input("BMI Category (0: Normal, 1: Overweight, 2: Obese, 3: Underweight)", min_value=0, max_value=3, value=0, step=1)
heart_rate = st.number_input("Heart Rate (beats per minute)", min_value=40, max_value=200, value=70, step=1)
daily_steps = st.number_input("Daily Steps", min_value=0, max_value=100000, value=5000, step=100)
systolic = st.number_input("Systolic Blood Pressure (mmHg)", min_value=80, max_value=200, value=120, step=1)
diastolic = st.number_input("Diastolic Blood Pressure (mmHg)", min_value=50, max_value=120, value=80, step=1)

# Process inputs
try:
    person_id = int(person_id) if person_id.isdigit() else 0
    input_data = np.array([[
        person_id, gender, age, occupation, sleep_duration,
        quality_of_sleep, physical_activity_level, stress_level,
        bmi_category, heart_rate, daily_steps, systolic, diastolic
    ]])
except Exception as e:
    st.error(f"Input processing error: {e}")

# Prediction button
if st.button("Predict"):
    try:
        prediction = model.predict(input_data)
        predicted_class = (prediction > 0.5).astype(int)[0][0]  # Binary classification logic

        if predicted_class == 1:
            st.error("The model predicts that you may have a sleep disorder.")
        else:
            st.success("The model predicts that you do not have a sleep disorder.")
    except Exception as e:
        st.error(f"Prediction error: {e}")
