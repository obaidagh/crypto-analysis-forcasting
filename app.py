import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import plotly.express as px
import plotly.graph_objects as go


plt.style.use('seaborn-whitegrid')
mpl.rcParams['figure.dpi'] = 300
st.set_page_config(page_title="StatsEuropa", page_icon="📈")

st.title('Cryptocurrencies price analysis and forcasting 📈')

tab_str = ['Analysis', 'Forcasting']
tab1, tab2 = st.tabs(tab_str)

with tab1:########################################################analysis######################
    option = st.selectbox(
        'Select coin?',
        (["BTC","ETH","ADA","XRP","MATIC","FTM"]))

    df = pd.read_csv(f"data/{option.lower()}_daily.csv")
    tab_str = ['Plotting', 'insights']
    tab1, tab2 = st.tabs(tab_str)   
    with tab1:#plots

        moving_avg_values = st.slider('Select 2 moving averages',20, 250, (50, 100))

        new_df= df[["time","open"]]

        new_df["moving1"]=new_df.open.rolling(moving_avg_values[0]).mean()
        new_df["moving2"]=new_df.open.rolling(moving_avg_values[1]).mean()

        new_df.fillna(0,inplace=True)

        new_df.rename(columns  = {
                        'open':'Open price',
                        'moving1': f'Moving average{moving_avg_values[0]}',
                        'moving2': f'Moving average{moving_avg_values[1]}'
                        },
                        inplace=True, errors='raise')

        #line plot
        fig = px.line(new_df, x="time", y=new_df.columns,
                hover_data={"time": "|%B %d, %Y"},

                title=f"{option} Daily Price")   

        st.write(fig) 

    with tab2:#insights
        col1, col2, col3 = st.columns(3)
        ath = df.open.max()
        atl = df.open.min() 
        with col1:
            st.markdown(f"<h3 style='background-color:#2bcc66;color: white;\
                              vertical-align:middle;text-align: center;'>All-time High</h3> <br>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='background-color:#e64356;color: white;\
                              vertical-align:middle;text-align: center;'>All-time Low</h3>", unsafe_allow_html=True)
        with col3:
            st.markdown(f"<h3 style='vertical-align:middle;text-align: center;'>{ath}</h3> <br>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='vertical-align:middle;text-align: center;'>{atl}</h3> <br>", unsafe_allow_html=True)