import os
import pandas as pd
from kite_trade import *
import datetime, time

enctoken = "0cTFZo63VI+0+WdW2m6+a3fLavr1juuj0SK5GQSlRoQSYS2QfEIL0M0L0B1ugNZ7ki4k0f56mnniNOx9yitUX007SyulWosmlaNIx+uAWr/hdwE8iSNUhA=="
kite = KiteApp(enctoken=enctoken)

instrument_token = 2478849
symbol = "KPITTECH"
interval = "5minute"
position = 'OUT'

while True:
    from_datetime = datetime.datetime.now() - datetime.timedelta(days=10)  # From last & days
    to_datetime = datetime.datetime.now()
    data = kite.historical_data(instrument_token, from_datetime, to_datetime, interval, continuous=False, oi=False)
    df = pd.DataFrame(data)
    df['50MA'] = df.close.rolling(window=50).mean()

    if df['close'].iloc[-2] > df['50MA'].iloc[-2] and df['close'].iloc[-3] <= df['50MA'].iloc[-3]:
        if position == 'OUT':
            order = kite.place_order(variety=kite.VARIETY_REGULAR,
                                     exchange=kite.EXCHANGE_NSE,
                                     tradingsymbol=symbol,
                                     transaction_type=kite.TRANSACTION_TYPE_BUY,
                                     quantity=1,
                                     product=kite.PRODUCT_MIS,
                                     order_type=kite.ORDER_TYPE_MARKET,
                                     price=None,
                                     validity=None,
                                     disclosed_quantity=None,
                                     trigger_price=None,
                                     squareoff=None,
                                     stoploss=None,
                                     trailing_stoploss=None,
                                     tag="TradeViaPython")
            print(order)
            position = 'LONG'

    elif df['close'].iloc[-2] < df['50MA'].iloc[-2] and df['close'].iloc[-3] >= df['50MA'].iloc[-3]:
        if position == 'LONG':
            sell = kite.place_order(variety=kite.VARIETY_REGULAR,
                                    exchange=kite.EXCHANGE_NSE,
                                    tradingsymbol=symbol,
                                    transaction_type=kite.TRANSACTION_TYPE_SELL,
                                    quantity=1,
                                    order_type=kite.ORDER_TYPE_MARKET,
                                    product=kite.PRODUCT_MIS)

            print(sell)
            position = 'OUT'

    else:
        print('no trade')
    time.sleep(60)

# data = pd.DataFrame(kite.ltp(f"NSE:{symbol}"))
# a = data.transpose()
# print(a.last_price)
