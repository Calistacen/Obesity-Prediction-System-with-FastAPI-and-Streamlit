import streamlit as st
import requests
import time


def main():
    st.set_page_config(page_title="Obesity Predictor", page_icon="🍽️")
    st.title("XXX Clinic Obesity Prediction App")
    st.markdown("#### Estimate a person's obesity category based on their lifestyle and dietary habits.")

    st.markdown("### **Patient Personal Information**")
    
    gender = st.radio("Gender", options=["Male", "Female"], 
                      format_func=lambda x: "♂️ Male" if x == "Male" else "♀️ Female",
                      horizontal=True)
    
    age = st.number_input("Age (years)", min_value=5, max_value=100, step=1)
    height = st.number_input("Height (meters) ", min_value=1.0, max_value=2.5, step=0.01, format="%.2f")
    weight = st.number_input("Weight (kilograms)", min_value=35.0, max_value=300.0, step=0.1, format="%.1f")

    st.markdown("### **Eating & Drinking Behavior**")

    ncp = st.slider("Number of Main Meals a Day", 1, 4, step=1)
    caec = st.select_slider("Do you eat between meals?", 
                            options=["No", "Sometimes", "Frequently", "Always"], 
                            help="From no snacking to frequent snacking")
    fcvc = st.slider("Vegetable Intake Frequency", 1, 3, step=1, help="Rarely (1) to Often (3)")
    ch2o = st.slider("Daily Water Intake", 1, 3, step=1, help="Rarely (1) to Often (3)")

    st.markdown("### Physical & Tech Activity")

    faf = st.slider("Physical Activity Frequency (weekly)", 0, 3, step=1, help="Rarely (0) to Often (3)")
    tue = st.slider("Daily Time on Tech Devices (daily)", 0, 3, step=1, help="Rarely (0) to Often (3)")
   

    if st.button("Predict Obesity Category"):
        input_load = {
            "Gender": gender,
            "Age": int(age),
            "Height": float(height),
            "Weight": float(weight),
            "NCP": float(ncp),
            "CAEC": caec,
            "FCVC": float(fcvc),
            "CH2O": float(ch2o),
            "FAF": float(faf),
            "TUE": float(tue)
        }
        
        with st.spinner("Analyzing your health profile..."):
            time.sleep(0.5)
            try:
                res = requests.post("http://127.0.0.1:8000/predict", json=input_load)
                output = res.json()
                if "prediction" in output:
                    category = output["prediction"]
                
                    st.markdown("### 🧠 **Prediction Result**")
                
                    # Show result with interaction
                    if category == "Normal_Weight":
                        st.success(f"✅ **{category}** — Great! You're within a healthy range.")
                    elif category == "Insufficient_Weight":
                        st.info(f"📉 **{category}** — You may need to improve your nutrition intake.")
                    elif "Overweight" in category:
                        st.warning(f"⚠️ **{category}** — Consider moderating calorie intake and increasing activity.")
                    elif "Obesity" in category:
                        st.error(f"🚨 **{category}** — There's a high risk. Medical attention is recommended.")
                    else:
                        st.info(f"ℹ️ **{category}** — Classification not recognized.")
                
                    # Add educational block
                    with st.expander("📚 What Do the Obesity Categories Mean?"):
                        st.markdown("""
                        - `Insufficient_Weight` → Body weight is too low.
                        - `Normal_Weight` → Healthy, ideal weight range.
                        - `Overweight_Level_I` → Slightly above normal weight.
                        - `Overweight_Level_II` → Moderately above normal weight.
                        - `Obesity_Type_I` → High body fat; lifestyle intervention recommended.
                        - `Obesity_Type_II` → Serious health risks; consult healthcare provider.
                        - `Obesity_Type_III` → Severe obesity; medical management required.
                        """)
                else:
                    st.error("❌ Prediction failed. Backend did not return a prediction.")
                    
            except Exception as e:
                st.error(f"🚫 Could not connect to backend: {e}")


        st.markdown("""
            <style>
            .watermark {
                position: fixed;
                bottom: 10px;
                left: 10px;
                color: white;
                background-color: rgba(0, 0, 0, 0.6); 
                padding: 8px 16px;
                font-size: 13px;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
                z-index: 9999;
                font-family: 'Segoe UI', sans-serif;
            }
            </style>
            <div class="watermark">Made by Calista Lianardi - 2702325880 - Final Exam</div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()




