import requests
import pandas as pd
import time
import math


def flatten_dict(my_dict):
    result = {}
    for key, value in my_dict.items():
        if isinstance(value, dict):
            result.update(flatten_dict(value))
        else:
            result[key] = value 
    return result

# it doesn't work for houlry because only pro-api have hourly interval
# change it if you have one :D
def coin_historical_data(symbol,end_time=int(time.time()),period='hourly',start_time=1367107200):
    # in coinmarketcap api "The current query limit is 10000 items"
    # so we have to divide the request into queries with size of 10000

    no_requests = (end_time - start_time)/(3600 *10000) #3600 for 1 h ,10000 for query limit
    quote_list=[]

    for i in range(math.ceil(no_requests)):
        start= start_time+(36000000*i)
        end = start_time+(36000000*(i+1))
        end = end if end < end_time else end_time
        #print(f"{i}, {time.asctime(time.gmtime(start))}, {time.asctime(time.gmtime(end))}")

        request_link = f"https://web-api.coinmarketcap.com/v1/cryptocurrency/ohlcv/historical?symbol={symbol}&time_end={end}&time_start={start}&time_period={period}"
        
        r = requests.get(url =request_link)
        r = r.json()
        quote_list.extend(r['data']['quotes'])

    h = list(map(flatten_dict, quote_list))
    
    df = pd.DataFrame(h)
    df["time_open"] = pd.to_datetime(df["time_open"],utc=None)
    df.drop(['time_close', 'time_low',"time_high","high","low"	,"timestamp"], axis = 1, inplace = True)
    df.fillna(0)
    return df


def main():

    symbols_list=["BTC","ETH","ADA","XRP","MATIC","FTM"]
    
    for symbol in symbols_list:
        df = coin_historical_data(symbol)
        print(symbol)
        df.to_csv(f"{symbol.lower()}_daily.csv", index=True)


main()
