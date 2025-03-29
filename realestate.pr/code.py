import streamlit as st
st.title("Stock prediction")

st.write("This is my new app that hopefully will predict the price of a stock")
st.header("Choose the ticker")

stocks = ["MU", "AAPL", "MSFT"]
choice1 = st.selectbox("Which of the following stocks you want to predict?", stocks)

days = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
choice2 = st.selectbox("select the number of days ahead (2 weeks max)", days)

button2 = st.button("predict")
