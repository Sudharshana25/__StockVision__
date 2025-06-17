import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
import pandas as pd
from stock_data import get_stock_data
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Fetch stock data
df = get_stock_data("AAPL", "2023-01-01", "2023-12-31")

# Prepare data: we'll predict 'Close' using days as X
df = df[['Date', 'Close']].dropna().reset_index(drop=True)
df['Date_ordinal'] = pd.to_datetime(df['Date']).map(pd.Timestamp.toordinal)

X = df[['Date_ordinal']]
y = df['Close']

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict
df['Predicted'] = model.predict(X)

# Plot
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Close'], label='Actual Close', color='blue')
plt.plot(df['Date'], df['Predicted'], label='Predicted Close (Linear)', color='red')
plt.title('Stock Price Prediction - Linear Regression')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
