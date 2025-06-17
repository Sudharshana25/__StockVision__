import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import matplotlib.pyplot as plt
from stock_data import get_stock_data
from statsmodels.tsa.arima.model import ARIMA

# Fetch data
df = get_stock_data("AAPL", "2023-01-01", "2023-12-31")
df = df[['Date', 'Close']].dropna().reset_index(drop=True)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Fit ARIMA model (p=5, d=1, q=0 as example)
model = ARIMA(df['Close'], order=(5, 1, 0))
model_fit = model.fit()

# Forecast
forecast = model_fit.forecast(steps=30)  # next 30 days

# Plot
plt.figure(figsize=(12, 6))
plt.plot(df['Close'], label='Actual Close')
forecast_index = pd.date_range(start=df.index[-1] + pd.Timedelta(days=1), periods=30)
plt.plot(forecast_index, forecast, label='Forecast (ARIMA)', color='orange')
plt.title('Stock Price Forecast - ARIMA Model')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
