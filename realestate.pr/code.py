import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

st.title("Welcome to a linear regression example")
st.write("There is an upcoming math exam next week, and you want to know the grade you will get based on the amount of hours you study  ")
st.write("The professor said in class that this exam will be very similar in terms of difficulty so the ratio grade-study hours shouldn't change too much compared to last exam ")
x = st.slider("how many hours have you studied?", min_value=0, max_value=10)
st.write("Hours studied:", x)
#regression
data = pd.read_csv("C:\\Users\\salbo\\Desktop\\Personal\\learning regressions\\linear\\regressiondata.csv")
x = data["STUDYTIME"].astype(float)
y = data["SCORE"].astype(float)

m , b = np.polyfit(x, y, 1)

yi = m * x + b
plt.scatter(x,y)
plt.plot(x, yi, linestyle='-', color="red", label=f"y = {m}x + {b}")

plt.text(min(x), max(y), f"m = {m:.2f}\nb = {b:.2f}", fontsize=12, color="blue")

st.write("y=")



st.title("Stock prediction")

st.write("This is my new app that hopefully will predict the price of a stock")
st.header("Choose the ticker")

stocks = ["MU", "AAPL", "MSFT"]
choice1 = st.selectbox("Which of the following stocks you want to predict?", stocks)
days = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
choice2 = st.selectbox("select the number of days ahead (2 weeks max)", days)

button2 = st.button("prediction")
