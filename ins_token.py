import os

import pandas as pd
from kite_trade import *
import datetime, time


enctoken = "0cTFZo63VI+0+WdW2m6+a3fLavr1juuj0SK5GQSlRoQSYS2QfEIL0M0L0B1ugNZ7ki4k0f56mnniNOx9yitUX007SyulWosmlaNIx+uAWr/hdwE8iSNUhA=="
kite = KiteApp(enctoken=enctoken)

print(kite.ltp(f"NSE:ADANIENT"))
    # instrument_token = 2953217
# from_datetime = datetime.datetime.now() - datetime.timedelta(days=1)  # From last & days
# to_datetime = datetime.datetime.now()
# data = kite.historical_data(instrument_token, from_datetime, to_datetime, '5minute', continuous=False, oi=False)
# df = pd.DataFrame(data)
# df['50MA'] = df.close.rolling(window=50).mean()
# print(df)