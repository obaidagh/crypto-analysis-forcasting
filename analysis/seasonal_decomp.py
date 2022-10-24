from statsmodels.tsa.seasonal import seasonal_decompose


def seasonal_decomp(df,column,model="additive"):
    sea_decomp_df = df.copy(deep=True)
    sea_decomp_df.index=sea_decomp_df.index.to_timestamp()

    s_dec_add = seasonal_decompose(sea_decomp_df[f'{column}'],model=model, period=1).plot()
    s_dec_add.set_size_inches(20, 8)
    return s_dec_add