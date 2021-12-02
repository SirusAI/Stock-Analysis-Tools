import pandas as pd
import datetime
import pandas_datareader.data as web
from prophet import Prophet

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime.today().strftime('%Y-%m-%d')

class Prodictor:
    def __init__ (self, ticker):

        ticker = ticker.upper()
        
        self.symbol = ticker #for future fuction
        
        try:
            stock = web.DataReader(ticker, 'yahoo', start, end)
        except Exception as e:
            print('Error Retrieving Data.')
            print (e)
            return
        df_a = stock.reset_index(col_level=0)
        df_a.rename(columns={'Date':'ds',"Adj Close":'y'}, inplace=True)
        df_a = df_a[['ds','y']]
        self.stock = df_a.copy()
    
    def predict(self,days):
        
        p = Prophet(daily_seasonality=False)
        
        p.fit(self.stock)
        
        future = p.make_future_dataframe(periods = days)
        
        forecast = p.predict(future)
        
        fig_a = p.plot(forecast,xlabel = self.symbol,ylabel = 'Price')
        
    
    def trend_analizer(self,days):
        
        p = Prophet(daily_seasonality=False)
        
        p.fit(self.stock)
        
        future = p.make_future_dataframe(periods = days)
        
        forecast = p.predict(future)

        fig_b = p.plot_components(forecast)
class Corranalyzer:
    
    def __init__(self, tickers):
        
        self.tickers = tickers
        
        if len(self.tickers) > 1:
            self.tickers = tickers
        else:
            print ("need more input")
        
    def matrixCorrl (self,highlight):
        
        highlight = highlight
        
        datacomp = web.DataReader(self.tickers,'yahoo', start = start, end = end)['Adj Close']
        
        pct_return = datacomp.pct_change()
                
        corr = pct_return.corr()
        
        self.corr = corr.copy()
        
        return corr.style.applymap(lambda x: 'background-color : orange' if x>highlight and x!=1 else '')
