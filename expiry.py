
import pandas as pd

af = pd.read_csv('https://api.kite.trade/instruments')
af=af[['name','segment','expiry','lot_size','tradingsymbol','strike','instrument_type','instrument_token','exchange_token','exchange']]
pairs = [('NFO-OPT','NIFTY'),('NFO-OPT','BANKNIFTY'),('NFO-OPT','FINNIFTY'),
         ('BFO-OPT','SENSEX'),('BFO-OPT','BANKEX'),('MCX-OPT','CRUDEOIL')]

df = pd.concat([af[(af['segment']==segment) & (af['name']==name)]
                for segment,name in pairs], ignore_index=True)
df['expiry'] = pd.to_datetime(df['expiry']).dt.strftime('%d-%m-%Y')
df = df.sort_values(by='expiry')
print(df[['name','segment','expiry','lot_size']])

