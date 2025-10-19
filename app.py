import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model and columns
model = pickle.load(open("car_price_model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

st.title("🚗 Car Price Prediction")
st.write("Enter details to predict the car's selling price")

# User inputs
car_models = [
    # BMW
    "BMW X5", "BMW 3 Series", "BMW X3", "BMW 5 Series", "BMW X1", "BMW Z4",
    
    # Audi
    "Audi A5", "Audi Q5", "Audi Q7", "Audi A6", "Audi A4", "Audi TT",
    
    # Mercedes-Benz
    "Mercedes Benz C class", "Mercedes Benz E class", "Mercedes Benz GLC",
    "Mercedes Benz S class", "Mercedes Benz CLA", "Mercedes Benz GLE",
    
    # Toyota
    "Toyota Corolla", "Toyota Camry", "Toyota RAV4", "Toyota Highlander", "Toyota Prius",
    
    # Honda
    "Honda Civic", "Honda Accord", "Honda CR-V", "Honda Pilot", "Honda Fit",
    
    # Ford
    "Ford Mustang", "Ford F-150", "Ford Explorer", "Ford Edge", "Ford Focus",
    
    # Tesla
    "Tesla Model 3", "Tesla Model S", "Tesla Model X", "Tesla Model Y", "Tesla Roadster", "Tesla Cybertruck",
    
    # Hyundai
    "Hyundai Tucson", "Hyundai Elantra", "Hyundai Santa Fe", "Hyundai Kona", "Hyundai Ioniq",
    
    # Kia
    "Kia Seltos", "Kia Sportage", "Kia Soul", "Kia Stinger", "Kia Carnival",
    
    # Nissan
    "Nissan Altima", "Nissan Sentra", "Nissan Maxima", "Nissan Rogue", "Nissan Murano"
]
car_model = st.selectbox("Car Model", car_models)
mileage = st.number_input("Mileage (in kms)", min_value=0, value=0, step=1000)
age = st.number_input("Age of the car (in years)", min_value=0, value=0, step=1)

# Convert user input to model format
user_data = pd.DataFrame(columns=columns)
user_data.loc[0] = 0
user_data.loc[0, "Mileage"] = mileage
user_data.loc[0, "Age(yrs)"] = age

if car_model == "Audi A5":
    user_data.loc[0, "Car Model_Audi A5"] = 1
elif car_model == "Mercedez Benz C class":
    user_data.loc[0, "Car Model_Mercedez Benz C class"] = 1
    
# Predict
if st.button("Predict Price"):
    prediction = model.predict(user_data)[0]
    inr = prediction*86
    st.success(f"Estimated Selling Price: ${round(prediction, 2)} (RS.{round(inr)}/-)")