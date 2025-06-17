import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from stock_data import get_stock_data, add_rsi
import plotly.graph_objects as go

# Fetch and add RSI
df = get_stock_data("AAPL", "2023-01-01", "2023-12-31")
df = add_rsi(df)

# Plot RSI
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df['Date'], y=df['RSI'],
    line=dict(color='purple', width=2),
    name='RSI'
))

# Overbought / Oversold levels
fig.add_hline(y=70, line=dict(color='red', dash='dash'), name='Overbought')
fig.add_hline(y=30, line=dict(color='green', dash='dash'), name='Oversold')

fig.update_layout(title='RSI (Relative Strength Index)', xaxis_title='Date', yaxis_title='RSI Value', yaxis_range=[0, 100])
fig.show()
