import streamlit as st

# Website ka Title aur Design
st.set_page_config(page_title="AI Fitness Pro", page_icon="💪")

st.title("💪 Smart BMI & Fitness Calculator")
st.write("Shahid Alam ka banaya hua pehla Web App")

# Input lene ke liye Boxes
weight = st.number_input("Aapka Weight (KG mein) dalein", min_value=1.0, value=70.0)
height_feet = st.slider("Aapka Height (Feet mein) chunein", 3.0, 7.0, 5.5)

# Calculation Logic
if st.button("BMI Calculate Karein"):
    height_meters = height_feet * 0.3048
    bmi = weight / (height_meters ** 2)
    
    st.subheader(f"Aapka BMI hai: {bmi:.2f}")
    
    if bmi < 18.5:
        st.warning("Status: Underweight (Diet acchi karein!)")
    elif 18.5 <= bmi < 24.9:
        st.success("Status: Normal/Fit (Zabardast! Aap fit hain.)")
    else:
        st.error("Status: Overweight (Workout shuru karein!)")
      
