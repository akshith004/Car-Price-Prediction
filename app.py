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
car_models = ['Maruti Swift Dzire VDI', 'Skoda Rapid 1.5 TDI Ambition', 'Honda City 2017-2020 EXi', 'Hyundai i20 Sportz Diesel', 'Maruti Swift VXI BSIII', 'Hyundai Xcent 1.2 VTVT E Plus', 'Maruti Wagon R LXI DUO BSIII', 'Maruti 800 DX BSII', 'Toyota Etios VXD', 'Ford Figo Diesel Celebration Edition', 'Renault Duster 110PS Diesel RxL', 'Maruti Zen LX', 'Maruti Swift Dzire VDi', 'Maruti Swift 1.3 VXi', 'Maruti Wagon R LXI Minor', 'Mahindra KUV 100 mFALCON G80 K8 5str', 'Maruti Ertiga SHVS VDI', 'Hyundai i20 1.4 CRDi Asta', 'Maruti Alto LX', 'Hyundai i20 2015-2017 Asta 1.4 CRDi']
# User inputs
car_model = st.selectbox("Car Model", car_models)
km_driven = st.number_input("Kilometers Driven", min_value=0, max_value=500000, step=1000)
fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "LPG", "Electric"])
seller_type = st.selectbox("Seller Type", ["Dealer", "Individual", "Trustmark Dealer"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.selectbox("Owner Type", ["First Owner", "Second Owner", "Third Owner", "Fourth & Above Owner", "Test Drive Car"])
mileage = st.number_input("Mileage (kmpl)", min_value=5.0, max_value=40.0, step=0.1)
engine = st.number_input("Engine (CC)", min_value=500, max_value=6000, step=50)
max_power = st.number_input("Max Power (bhp)", min_value=20.0, max_value=600.0, step=1.0)
seats = st.number_input("Seats", min_value=2, max_value=10, step=1)
car_age = st.number_input("Car Age (in years)", min_value=0, max_value=30, step=1)

# --- Convert Input to Model Format ---
input_data = pd.DataFrame(columns=columns)
input_data.loc[0] = 0  # initialize with zeros

# Fill numeric values
input_data.loc[0, "km_driven"] = km_driven
input_data.loc[0, "mileage"] = mileage
input_data.loc[0, "engine"] = engine
input_data.loc[0, "max_power"] = max_power
input_data.loc[0, "seats"] = seats
input_data.loc[0, "car_age"] = car_age

# Handle categorical encoding (dummy variables)
for col in columns:
    if f"fuel_{fuel}" == col:
        input_data.loc[0, col] = 1
    if f"seller_type_{seller_type}" == col:
        input_data.loc[0, col] = 1
    if f"transmission_{transmission}" == col:
        input_data.loc[0, col] = 1
    if f"owner_{owner}" == col:
        input_data.loc[0, col] = 1

# --- Predict ---
if st.button("🔍 Predict Price"):
    try:
        prediction = model.predict(input_data)[0]
        st.success(f"💰 Estimated Selling Price: ₹{round(prediction, 2)} lakhs")
    except Exception as e:
        st.error(f"Error while predicting: {e}")
        st.write("Check if your column names and data format match the model’s training data.")