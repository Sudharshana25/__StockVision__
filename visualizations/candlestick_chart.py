import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from stock_data import get_stock_data, add_moving_averages
import plotly.graph_objects as go

# Fetch + add SMA
df = get_stock_data("AAPL", "2023-01-01", "2023-12-31")
df = add_moving_averages(df)

# Plot candlestick
fig = go.Figure()

fig.add_trace(go.Candlestick(
    x=df['Date'],
    open=df['Open'],
    high=df['High'],
    low=df['Low'],
    close=df['Close'],
    name='Candlestick'
))

# Plot SMA lines
fig.add_trace(go.Scatter(
    x=df['Date'], y=df['SMA_20'],
    line=dict(color='blue', width=1.5),
    name='SMA 20'
))

fig.add_trace(go.Scatter(
    x=df['Date'], y=df['SMA_50'],
    line=dict(color='orange', width=1.5),
    name='SMA 50'
))

fig.update_layout(title='Stock with SMA 20 & SMA 50', xaxis_title='Date', yaxis_title='Price')
fig.show()
