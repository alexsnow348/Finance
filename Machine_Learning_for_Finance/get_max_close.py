import pandas as pd
import matplotlib.pyplot as plt
def get_max_close(symbol):
    """ Return the maximum closing value for stock indicated by symbol"""
    df = pd.read_csv("./data/{}.csv".format(symbol))

    return df['Close'].max()

def plot_data(symbol):
    df = pd.read_csv("./data/{}.csv".format(symbol))
    df[['Adj Close','Close']].plot()
    plt.show()

def test_run():
    """Function called by test run"""
    for symbol in ['AAPL','HCP']:
        # print('Max Close')
        # print(symbol,get_max_close(symbol))
        plot_data(symbol)

if __name__ == '__main__':
    test_run()
