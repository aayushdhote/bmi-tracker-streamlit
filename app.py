import streamlit as st
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

st.set_page_config(page_title="BMI & Health Tracker", layout="centered")

st.title("🩺 BMI & Health Calculator")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=1, max_value=120, step=1)
gender = st.selectbox("Select your gender", ["Male", "Female", "Other"])
height = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, step=0.1)
weight = st.number_input("Weight (kg)", min_value=10.0, max_value=300.0, step=0.1)

if st.button("Calculate BMI"):
    if height > 0:
        height_m = height / 100
        bmi = weight / (height_m ** 2)
        st.success(f"{name}, your BMI is *{bmi:.2f}*")
        logging.info(f"BMI calculated for {name} (Age: {age}, Gender: {gender}) - Height: {height} cm, Weight: {weight} kg, BMI: {bmi:.2f}")

        if bmi < 18.5:
            st.info("You are *Underweight*")
        elif 18.5 <= bmi < 24.9:
            st.success("You are in the *Normal* weight range")
        elif 25 <= bmi < 29.9:
            st.warning("You are *Overweight*")
        else:
            st.error("You are in the *Obese* category")
    else:
        st.error("Please enter a valid height.")
