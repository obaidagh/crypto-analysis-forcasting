from numpy import size
import streamlit as st
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

from data import data_cleaning
from analysis import acf_pacf_plot,hist_plot,qq_plot,seasonal_decomp
from streamlit_funcs.insights import insights
from streamlit_funcs.prophet_res import prophet_res
from streamlit_funcs.arima_st import arima_st

from prophet.serialize import  model_from_json
from prophet.plot import plot_plotly, plot_components_plotly

st.set_page_config(page_title="Crypto", page_icon="📈",layout='wide')
st.title('Crypto Analysis and Forcasting 📈')

tab_str = ['Analysis', 'Forcasting']
tab1, tab2 = st.tabs(tab_str)


########################################################analysis########################################################
with tab1:
    option = st.selectbox(
        'Select coin?',
        (["BTC","ETH","ADA","XRP","MATIC","FTM"]))

    _,df,_,df_test=data_cleaning(f"{option.lower()}",split_point=-1)


    tab_str = ['Time series','Histogram','Autocorrelation','QQ','Seasonal decompose', 'Insights']
    tab_ts,tab_hist,tab_acf,tab_qq,tab_seas, tab_ins = st.tabs(tab_str)
    with tab_ts:
        ts_col1, ts_col2, = st.columns(2)

        moving_avg_1 = ts_col1.text_input("Enter first moving average", value="12")
        moving_avg_2 = ts_col2.text_input("Enter second moving average", value="365")
        df["moving1"]=df.price.rolling(f"{moving_avg_1}D").mean()
        df["moving2"]=df.price.rolling(f"{moving_avg_2}D").mean()

        fig = px.line(df, x=df.index.to_timestamp(), y=['price','moving1','moving2'],
            title=f"{option} Daily Price",width=1400,height=600)


        st.write(fig)

    with tab_hist:
        st.write(hist_plot(df))
    with tab_acf:
        st.write(acf_pacf_plot(df.price,"Prices",lags=90))
        st.write(acf_pacf_plot(df.returns,"Returns",lags=90))
    with tab_qq:
        st.write(qq_plot(df))
    with tab_seas:
        st.write(seasonal_decomp(df,"price"))

    with tab_ins:#insights
        insights(df)


########################################################analysis########################################################
with tab2:
    st.warning('Currently only for bitcoin')
    tab_str = ['Prophet','ARIMA Family Prices','ARIMA Family Returns']
    tab_prophet,tab_arima_price,tab_arima_returns = st.tabs(tab_str)
    

    #..................prophet model...........#
    with tab_prophet:        
        prophet_res(df_test)
    with tab_arima_price:
        arima_st(is_price=True)
    with tab_arima_returns:
        arima_st(is_price=False)
        