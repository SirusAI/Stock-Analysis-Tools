# Stock-Analysis-Tools
Prophet Stock Price Prediction
This information contained on this notebook and the resources avaiable for dowload through this website is not intended as, and shall not be understood or contruced as, financial advice!I developed this tool mainly to gain more experience in time series analysis and object-oriented programming. The goal is to combine different machine learning methods for stock analysis. I will occasionally update this project by adding more functions. (*** Stock historical price data is from Yahoo Finance)
# Libraries for the project
* [Pandas](https://pandas.pydata.org)
* [Pandas-datareader](https://pandas-datareader.readthedocs.io/en/latest)
* [Datetime](https://docs.python.org/3/library/datetime.html)
* [Prophet](https://facebook.github.io/prophet/docs/installation.html#installation-in-python)
* [Matplotlib](https://matplotlib.org)
# Results from the Prophet prediction
## Single Stock Analysis

```
from metaprodictor import Prodictor

ticker = 'spy' 
days = 365 
test_ticker = Prodictor(ticker) 
```
### Example of Stock Trend Analysis

```
test_ticker.trend_analizer(365)
```
* Seasonal Trend

![](image/Porphet_Trend_analysis.png)

### Example of Stocks Open To Close Return Stats Analysis

```
test_ticker.oTc_return()
```
* Winning Rate = Daily_Return(>0)/total trading days; Total_gains = accumulate all positive % returns (close to close)

![](image/opentoclosestat.png)

* Open to Close Return (%) Chart

![](image/opentoclosechart.png)

### Example of Stocks Close To Close Return Stats Analysis

```
test_ticker.cTc_return()
```
* Winning Rate = Daily_Return(>0)/total trading days; Total_gains = accumulate all positive % returns (close to close)

![](image/closetoclosestat.png)

* Close to Close Return (%) Chart

![](image/closetoclosechart.png)

### Example of Stocks Daily Return Correlation Matrix for Energy Stocks
```
from metaprodictor import Corranalyzer

ticker_group = ['DVN','CLR','MRO','FANG','CVE','TRGP','SSL','EOG','COP','IMO'] #Put your stocks here
highlight = 0.78 # highlight if correlation is greater than 0.78

b = Corranalyzer(ticker_group)
b.matrixCorrl(highlight)
```
## Portfolio Analysis
### Correlation Matrix for Energy Stocks

![](image/CORRELATION.png)


### Daily Return Risk/Return Chart and Concise Summary of the Past Performance
```
b.riskRank()
```
* Ranking from Highest Risk

![](image/riskc.png)

* Risk VS Return

![](image/ranking.png)
