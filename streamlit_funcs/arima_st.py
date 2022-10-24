import streamlit as st
import pandas as pd
import plotly.express as px

def arima_st(is_price):
    pred= pd.read_csv('predictions.csv')
    if is_price:
        st.write(px.line(pred,x=pred.date,y=["price","arima_prices"]))

    else:
        st.write(px.line(pred,x=pred.date,y=["returns","ar_returns","ma_returns","arma_returns"]))

