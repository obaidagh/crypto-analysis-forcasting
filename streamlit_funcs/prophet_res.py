import streamlit as st
import plotly.graph_objects as go
from prophet.serialize import  model_from_json
from prophet.plot import plot_plotly, plot_components

def prophet_res(df_test):
    df_test.reset_index(inplace=True)

    with open('models/saved/prophet_serialized_model.json', 'r') as fin:
        model = model_from_json(fin.read())  # Load mode
        
    future = model.make_future_dataframe(periods=448)
    forecast = model.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

    tab_str = ['Predictions','Components']
    tab_pred,tab_comp = st.tabs(tab_str)
    
    prophet_fig= plot_plotly(model, forecast, figsize = (1400, 600))
    
    with tab_pred:
        
        st.write(prophet_fig)
    with tab_comp:
        st.write(model.plot_components(forecast))