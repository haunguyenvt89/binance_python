from cgi import test
from unittest import result
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
from binance.enums import KLINE_INTERVAL_1DAY
# import pandas as pd

api_key = "wh9MGeix56gfB3f7fVYszrWUSdXbcGyIu7D2Evx1JScZ1oMGa8FThGfWFJMwu5Nk"
api_secret = "PpeVgmzqZdIGb6CLdtbHx8D3X2HBhKzcNw2BKuuYOOsU3S095r2JC3ZUgsqBOQsn"
client = Client(api_key, api_secret)

ada_ticker = client.futures_symbol_ticker(symbol='ADAUSDT')
ada_ticker_1d = client.futures_historical_klines(
    symbol='ADAUSDT',
    interval='1d',
    start_str='2021-01-18',
    end_str='2022-01-19'
)
def test_ada():
    print("ADA Tickers")
    print(ada_ticker)

def test_ada_1d():
    print("ADA Tickers in 1d")
    print(ada_ticker_1d)

# def test_pandas_ada():
#     df = pd.DataFrame(client.futures_historical_klines(
#         symbol='ADAUSDT',
#         interval='1d',
#         start_str='2022-01-18',
#         end_str='2022-01-19'
#     ))
#     df.head()

# def drop_unnecessary_frame_ada():
#     df = pd.DataFrame(client.futures_historical_klines(
#         symbol='ADAUSDT',
#         interval='1d',
#         start_str='2022-01-18',
#         end_str='2022-01-19'
#     ))
#     df = df.iloc[:, :6]
#     # ascribe names to columns
#     df.columns = ['date', 'open', 'high', 'low', 'close', 'volume']
#     # convert timestamp to date format and ensure ohlcv are all numeric
#     df['date'] = pd.to_datetime(df['date'], unit='ms')
#     for col in df.columns[1:]:
#         df[col] = pd.to_numeric(df[col])
#     df.head()

def test_buy_iota_2_limit():
    result = client.futures_create_order(
        symbol='IOTAUSDT',
        type='LIMIT',
        price=0.5,
        side='BUY',
        positionSide='LONG',
        timeInForce='GTC',
        quantity=10
    )
    print(result)

def test_sell_iota_2_limit():
    result = client.futures_create_order(
        symbol='IOTAUSDT',
        type='LIMIT',
        timeInForce='GTC',
        price=2,
        side='SELL',
        positionSide='SHORT',
        quantity=10
    )
    print(result)

def test_buy_iota_2_trailing():
    result = client.futures_create_order(
        symbol='IOTAUSDT',
        type='TRAILING_STOP_MARKET',
        price=0.5,
        side='BUY',
        positionSide='LONG',
        callbackRate=3,
        timeInForce='GTC',
        quantity=10
    )
    print(result)
def test_get_balance():
        result = client.get_account_api_permissions(

        )
        print(result)

def test_get_hight_low():
    result  = client.futures_historical_klines('BTCUSDT', KLINE_INTERVAL_1DAY, '2022-02-12')
    print(result)
# =========
# test_ada()
# test_ada_1d()
# test_pandas_ada()
# test_buy_iota_2_limit()
# test_sell_iota_2_limit()

#test_buy_iota_2_trailing()
# test_sell_iota_2_limit()
test_get_hight_low()
