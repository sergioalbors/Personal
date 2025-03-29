import streamlit as st
st.title("Stock prediction")

st.write("This is my new app that hopefully will predict the price of a stock")
st.header("Choose the ticker")

stocks = ["MU", "AAPL", "MSFT"]
choice1 = st.selectbox("Which of the following stocks you want to predict?", stocks)

