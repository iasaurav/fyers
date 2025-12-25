
import pandas as pd

df = pd.read_csv('https://api.kite.trade/instruments')
pairs = [('NFO-OPT','NIFTY'),('NFO-OPT','BANKNIFTY'),('NFO-OPT','FINNIFTY'),
         ('BFO-OPT','SENSEX'),('BFO-OPT','BANKEX'),('MCX-OPT','CRUDEOIL')]

option = pd.concat([df[(df.segment==s)&(df.name==n)].head(1) for s,n in pairs])
option['expiry'] = pd.to_datetime(option['expiry']).dt.strftime('%d-%m-%Y')
option = option.sort_values(by='expiry')
option=option.drop(columns=['instrument_token','tick_size', 'last_price'])
print(option)

