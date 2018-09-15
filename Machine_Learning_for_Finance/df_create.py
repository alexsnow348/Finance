''' Build dataframe from different data source '''

import pandas as pd
from datetime import datetime as dt
import matplotlib.pyplot as plt

def read_from_csv_to_df(symbol):
    """ Return dataframe for stock indicated by symbol"""
    df = pd.read_csv("./data/{}.csv".format(symbol),index_col="Date",
     parse_dates=True,usecols=['Date','Adj Close'],na_values=['nan'])
    return df
def join_dfs(start_date,end_date,symbol_list):
    start_date = dt.strptime(start_date,'%Y-%m-%d')
    end_date = dt.strptime(end_date,'%Y-%m-%d')
    dates = pd.date_range(start_date,end_date)
    # dates = [date.strftime('%Y-%m-%d') for date in dates]
    df1= pd.DataFrame(index=dates)
    if 'SPY' not in symbol_list:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')
    for symbol in symbol_list:
        df = read_from_csv_to_df(symbol)
        df = df.rename(columns={'Adj Close':symbol})
        df1 = df1.join(df,how='inner')
        if symbol == 'SPY':
            df1 = df1.dropna(subset=['SPY'])
    return df1
def get_data(symbol_list):
    df1 = pd.DataFrame()
    if 'SPY' not in symbol_list:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')
    for symbol in symbol_list:
        df = read_from_csv_to_df(symbol)
        df = df.rename(columns={'Adj Close':symbol})
        df1 = df.join(df1)
        if symbol == 'SPY':
            df1 = df1.dropna(subset=['SPY'])
    return df1
def slice_ops(symbol_list):
    start_date = '2017-09-14'
    end_date = '2018-09-14'
    df = join_dfs(start_date,end_date,symbol_list)
    # Slice by row range (dates) using DataFrame.loc[] selector
    df_rs = df.loc['2018-01-10':'2018-01-31']
    df_cs = df[['IBM','SPY']]
    df_rcs = df.loc['2018-01-10':'2018-01-31',['IBM','SPY']]
    return df_rcs
def normalize_df(df):
    ''' Normalize stock prices using the first row of the dataframe'''
    return df/df.iloc[0,:]

def plot_data(df,title='Stock prices'):
    '''Plot stock prices'''
    ax = df.plot(title=title)
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    plt.show()

def test_run():
    symbol_list = ['SPY','GLD','AAPL','IBM']
    # df = slice_ops(symbol_list)
    df = get_data(symbol_list)
    df = normalize_df(df)
    plot_data(df)
    #

if __name__ =='__main__':
    test_run()
