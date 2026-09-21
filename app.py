import streamlit as st
import os
from diet import bmi_calculator, bmr_calculator, tdee_calculator, calorie_target
# st.page_setup(page_title="Health Assistant", page_icon="  ", layout="wide")
st.title("AI Health Assistant")
# st.header(" Health Information")
st.write("Personal Health Assistance and Diet Recommendation Agent")
st.header("Health Information")
st.sidebar.header("Your Information")

gender=st.sidebar.selectbox("Gender",["Male", "Female"])
age=st.sidebar.number_input ("Age",1,100)
weight= st.sidebar.number_input("Weight(kg)",1,20)
height= st.sidebar.number_input("height(cm)",100,200)
activity= st.sidebar.selectbox("Activity",["Sedentary",
                     "Lightly Active",
                     "Moderately Active",
                     "Very Active",
                     "Extra Active"])
aim=st.sidebar.selectbox("Aim", ["weight maintain", "weight loss", "weight gain"])

# ------------------------------------------------------------------------------ #

bmi=bmi_calculator(weight, height)
bmr=bmr_calculator(gender,age, weight, height)
tdee=tdee_calculator(bmr,activity)
calories=calorie_target(tdee,aim)

# -------------------------------------------#
col1,col2,col3,col4=st.columns(4)

col1.metric("BMI",bmi)
col2.metric("BMR",bmr)
col4.metric("TDEE",tdee)
col3.metric("Calorie Target",calories)
