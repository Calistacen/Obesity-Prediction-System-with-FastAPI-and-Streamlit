# Obesity Prediction System — FastAPI + Streamlit
This is an end-to-end machine learning deployment project that predicts a person’s **obesity category** based on their lifestyle and physical characteristics.  
This project integrates a **FastAPI backend** and a **Streamlit frontend** powered by a **Random Forest Classifier** model.


## Project Overview
This project are made to fulfill the Final Exam for Model Deployment subject in 4th Semester.
This project could be aimmed to help health professionals and fitness clinics **estimate obesity risk levels** interactively, which count as technology innovation in medical field 
Users enter personal and lifestyle data — such as diet habits, exercise frequency, and water intake — and receive an instant obesity classification.


## System Architecture

| Component | Description |
|------------|-------------|
|  **Model** | Random Forest Classifier (`ObessityRF.pkl`) trained on obesity dataset |
|  **Backend (API)** | FastAPI app (`FinalExamMD_BackEndAPI_2702325880.py`) that handles prediction requests |
|  **Frontend (UI)** | Streamlit app (`FinalExamMD_StreamlitFrontEnd_2702325880.py`) that provides a clean, interactive interface |
|  **Testing** | Unit testing, API testing, and UI-level validation conducted to ensure robustness |


##  Input Parameters

| Feature | Description |
|----------|-------------|
| Gender | Male / Female |
| Age | Age in years |
| Height | Height (in meters) |
| Weight | Weight (in kilograms) |
| NCP | Number of main meals per day |
| CAEC | Eating between meals frequency (No, Sometimes, Frequently, Always) |
| FCVC | Vegetable consumption frequency (1–3) |
| CH2O | Water intake frequency (1–3) |
| FAF | Physical activity frequency (0–3) |
| TUE | Technology use frequency (0–3) |


##  Output Categories

| Label | Meaning |
|--------|----------|
| `Insufficient_Weight` | Below healthy weight |
| `Normal_Weight` | Healthy range |
| `Overweight_Level_I` | Slightly above normal |
| `Overweight_Level_II` | Moderately above normal |
| `Obesity_Type_I` | High body fat; intervention recommended |
| `Obesity_Type_II` | Serious health risk |
| `Obesity_Type_III` | Severe obesity; medical management required |



##### This project are made for educational purposes only. By Calista.L
