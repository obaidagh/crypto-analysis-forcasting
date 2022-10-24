import pandas as pd

def data_cleaning(coin,split_point=-447):
    df_orginal = pd.read_csv(f"data/{coin}_daily.csv", parse_dates = ['time'])
    df = df_orginal.copy(deep=True)

    df.rename(columns={
        'time':'date',
        'open':'price',
    } ,inplace=True)

    df.index = pd.DatetimeIndex(df.date).to_period('D')
    df.drop(columns=['date','close','market_cap','volume'],inplace=True)
    df["returns"] = df.price.pct_change(1).mul(100)
    df.dropna(inplace=True)
    df_train = df.iloc[:split_point] 
    df_test  = df.iloc[split_point:]

    return df_orginal,df,df_train,df_test