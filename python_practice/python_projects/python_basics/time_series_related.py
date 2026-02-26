#1. The Mock Dataset Generator


#Run this in your notebook to create the df_stocks you'll be working with:

#Python
import pandas as pd
import numpy as np

# Create 500 days of dates for two stocks
dates = pd.date_range(start='2024-01-01', periods=500, freq='D')
tickers = ['AAPL', 'GOOGL']

data = []
for ticker in tickers:
    # Generate a random walk for prices
    start_price = 150 if ticker == 'AAPL' else 140
    prices = start_price + np.cumsum(np.random.randn(500)) 
    
    for date, price in zip(dates, prices):
        data.append([date, ticker, price])

df_stocks = pd.DataFrame(data, columns=['Date', 'Ticker', 'Close'])
# daily returns 
df_stocks['daily_returns'] = df_stocks.groupby('Ticker')['Close'].transform(lambda x: x.pct_change)
#volatality
# The 'transform' method is the cleanest way to map rolling stats back to the original rows
df_stocks['volatility'] = (
    df_stocks.groupby('Ticker')['Close']
    .transform(lambda x: x.rolling(window=30).std())
)

df_stocks['SMA_50'] = (
    df_stocks.groupby('Ticker')['Close']
    .transform(lambda x: x.rolling(window=50).mean())
)
df_stocks['SMA_200'] = (
    df_stocks.groupby('Ticker')['Close']
    .transform(lambda x: x.rolling(window=200).mean())
)

df_stocks["signal"] = np.where( df_stocks['SMA_50'] > df_stocks['SMA_50'] ,1, 0)



'''
2. Your Task Instructions (Step-by-Step)

Here is exactly what you need to write in your notebook today to master window functions:

Step 1: Daily Returns (The pct_change tool)

You need to calculate how much the stock went up or down compared to the day before. Note: Use groupby('    ') so AAPL's price isn't compared to GOOGL's price!

Step 2: Volatility (The rolling tool)

Volatility is just the Standard Deviation of returns.

Use a 30-day window: .rolling(window=30).std().

High volatility means the "swings" are getting wider (riskier).

Step 3: The Golden Cross (The rolling + np.where tool)

This is a classic technical analysis signal.

Calculate SMA_50 (Simple Moving Average).

Calculate SMA_200.

Create a column Signal where it is 1 if SMA_50 > SMA_200 and 0 otherwise.
'''