import streamlit as st

def insights(df):
    ins_col1, ins_col2, ins_col3 = st.columns(3)
    ath_price = df.price.max()
    atl_price = df.price.min() 
    ath_returns = df.returns.max()
    atl_returns = df.returns.min() 
    with ins_col1:
        st.markdown(f"<h3 style='background-color:#2bcc66;color: white;\
                            vertical-align:middle;text-align: center;'>All-time High Prices</h3> <br>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='background-color:#e64356;color: white;\
                            vertical-align:middle;text-align: center;'>All-time Low Prices</h3><br>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='background-color:#2bcc66;color: white;\
                            vertical-align:middle;text-align: center;'>All-time High Returns</h3> <br>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='background-color:#e64356;color: white;\
                            vertical-align:middle;text-align: center;'>All-time Low Returns</h3>", unsafe_allow_html=True)
    with ins_col3:
        st.markdown(f"<h3 style='vertical-align:middle;text-align: center;'>{ath_price}</h3> <br>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='vertical-align:middle;text-align: center;'>{atl_price}</h3> <br>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='vertical-align:middle;text-align: center;'>%{ath_returns}</h3> <br>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='vertical-align:middle;text-align: center;'>%{atl_returns}</h3> <br>", unsafe_allow_html=True)