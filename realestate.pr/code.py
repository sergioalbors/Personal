import streamlit as st
st.title("Stock prediction")

st.write("This is my new app that hopefully will predict the price of a stock")
st.header("Choose the ticker")
choice1 = st.selectbox("Which of the following stocks you want to predict?")
    ("MU", "MSFT", "AAPL")
button1 = st.button("Predict")