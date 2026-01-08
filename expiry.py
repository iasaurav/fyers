
import pandas as pd

df = pd.read_csv('https://api.kite.trade/instruments')
df=df[['name','segment','expiry','lot_size','tradingsymbol','strike','instrument_type','instrument_token','exchange_token','exchange']]
pairs = [('NFO-OPT','NIFTY'),('NFO-OPT','BANKNIFTY'),('NFO-OPT','FINNIFTY'),
         ('BFO-OPT','SENSEX'),('BFO-OPT','BANKEX'),('MCX-OPT','CRUDEOIL')]

option = pd.concat([df[(df['segment']==segment) & (df['name']==name)].head(1)
                for segment,name in pairs], ignore_index=True)
option['expiry'] = pd.to_datetime(option['expiry']).dt.strftime('%d-%m-%Y')
option = option.sort_values(by='expiry')
print(option[['name','segment','expiry','lot_size']])

