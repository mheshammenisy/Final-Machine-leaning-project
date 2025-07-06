import streamlit as st
import pandas as pd
import joblib

# Load model and features
model = joblib.load('personality3_model.pkl')

# Title
st.title("🧠 Personality Prediction App")
st.markdown("Select your behavior scores below and click **Predict** to see your personality type.")

# Input fields with dropdowns for each feature
Time_spent_Alone = st.selectbox("Time Spent Alone", list(range(0, 16)))
Stage_fear = st.selectbox("Stage Fear (0 = No, 1 = Yes)", [0, 1])
Drained_after_socializing = st.selectbox("Drained After Socializing (0 = No, 1 = Yes)", [0, 1])


# Create a DataFrame with the same column order as training
input_data = pd.DataFrame([{
    'Time_spent_Alone': Time_spent_Alone,
    'Stage_fear': Stage_fear,
    'Drained_after_socializing': Drained_after_socializing,
  
}])

# Predict
if st.button("Predict Personality"):
    prediction = model.predict(input_data)[0]
    label = "Introvert" if prediction == 1 else "Extrovert"
    st.success(f"🧬 You are predicted to be: **{label}**")
