import time

import pandas as pd
from kite_trade import *
import mplfinance as mpf
import datetime

# user_id = "VB9615"       # Login Id
# password = "Priyansh@18"      # Login password
# twofa = "904961"         # Login Pin or TOTP
#
# enctoken = get_enctoken(user_id, password, twofa)
# kite = KiteApp(enctoken=enctoken)

enctoken = "U2lOYTxZpKeANR8UvN2uqwpsLEIjkU/Ts541wxWb+RbFu1qRioosQBJRyqUFyOdGfWVD8HMqImtPvS0csPiG9DfpD9vNujIo1XHRquLO9sru446nmrLA/Q=="
kite = KiteApp(enctoken=enctoken)

# print(kite.margins())
# print(kite.ltp("NSE:FSL"))


# Get Historical Data
#
instrument_token = 3661825
from_datetime = datetime.datetime.now() - datetime.timedelta(days=10)     # From last & days
to_datetime = datetime.datetime.now()
interval = "5minute"

data = kite.historical_data(2952193, from_datetime, to_datetime, interval, continuous=False, oi=False)
df = pd.DataFrame(data)
print(df)
#print(df.close.rolling(window=7).mean().head(20))
# while True:
#     mpf.plot(df, type='candle', volume=True, style='yahoo', mav=(10, 20))
#     time.sleep(5)

#
# mpf.plot(df, type='candle', volume=True, style='yahoo', mav=(10,20))


# data = pd.DataFrame(kite.ltp("NSE:FSL"))
# a = data.transpose()
# print(a.last_price)