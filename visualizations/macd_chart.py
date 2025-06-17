import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from stock_data import get_stock_data, add_macd
import plotly.graph_objects as go

# Get data with MACD
df = get_stock_data("AAPL", "2023-01-01", "2023-12-31")
df = add_macd(df)

# Plot MACD and Signal Line
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df['Date'], y=df['MACD'],
    line=dict(color='blue', width=2), name='MACD'
))

fig.add_trace(go.Scatter(
    x=df['Date'], y=df['Signal_Line'],
    line=dict(color='orange', width=2, dash='dash'), name='Signal Line'
))

# Optional: Add MACD histogram
fig.add_trace(go.Bar(
    x=df['Date'], y=(df['MACD'] - df['Signal_Line']),
    name='Histogram', marker_color='lightblue', opacity=0.5
))

fig.update_layout(title='MACD Indicator', xaxis_title='Date', yaxis_title='MACD Value')
fig.show()
