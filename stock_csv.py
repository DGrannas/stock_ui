from pandas_datareader import data as pdr
import pandas as pd

#Read in ticker symbols for S&P 500
data = pd.read_csv("tickers.csv")
data_list = data["ticker"].tolist()

#Get data from all stocks in stock_data folder
def get_data (*tickers):

    main_df = pd.DataFrame()
    for count, ticker in enumerate(tickers):
        try:
            df = pd.read_csv("./stock_data/{}.csv".format(ticker))
            df.set_index("Date", inplace=True)
            df.rename(columns = {"Adj Close": ticker}, inplace=True)
            df.drop(["Open","High","Low","Close","Volume"],1, inplace=True)

            if main_df.empty:
                main_df = df
            else:
                main_df = main_df.join(df, how="outer")
        except:
            print("{} Not found".format(ticker))
        if count % 10 == 0:
            print(count)

    print(main_df.head())
    main_df.to_csv("sp500_joined_closes.csv")

get_data(data_list)
