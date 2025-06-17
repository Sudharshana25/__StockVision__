import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from stock_data import get_stock_data
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM

# Load & prepare data
df = get_stock_data("AAPL", "2020-01-01", "2023-12-31")
df = df[['Date', 'Close']].dropna().reset_index(drop=True)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Normalize Close prices
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(df[['Close']])

# Prepare sequences (60-day windows)
X, y = [], []
for i in range(60, len(scaled_data)):
    X.append(scaled_data[i-60:i, 0])
    y.append(scaled_data[i, 0])

X, y = np.array(X), np.array(y)
X = X.reshape((X.shape[0], X.shape[1], 1))  # reshape for LSTM

# Build model
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(X.shape[1], 1)))
model.add(LSTM(units=50))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X, y, epochs=10, batch_size=32, verbose=1)

# Predict on last 60 days
last_60 = scaled_data[-60:]
last_60 = last_60.reshape((1, 60, 1))
predicted_price = model.predict(last_60)
predicted_price = scaler.inverse_transform(predicted_price)

# Display result
print(f"\n🔮 Predicted next closing price: ₹{predicted_price[0][0]:.2f}")

# Optional: Visualize actual vs predicted on train data
train_preds = model.predict(X)
train_preds = scaler.inverse_transform(train_preds.reshape(-1, 1))
actual_prices = scaler.inverse_transform(y.reshape(-1, 1))

plt.figure(figsize=(12, 6))
plt.plot(actual_prices, label='Actual Price')
plt.plot(train_preds, label='Predicted (Train)', color='red')
plt.title('LSTM Model - Actual vs Predicted (Training Set)')
plt.xlabel('Time Step')
plt.ylabel('Price')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
