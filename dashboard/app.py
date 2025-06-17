import streamlit as st
from stock_data import get_stock_data
import matplotlib.pyplot as plt

st.title("📈 StockVision - Real-time Stock Dashboard")

# Stock selection input
ticker = st.text_input("Enter Stock Symbol (e.g., AAPL, TCS.NS):", "AAPL")
start_date = st.date_input("Start Date", value=pd.to_datetime("2023-01-01"))
end_date = st.date_input("End Date", value=pd.to_datetime("2023-12-31"))

# Load data
if st.button("Fetch Data"):
    df = get_stock_data(ticker, str(start_date), str(end_date))
    st.write(f"Showing data for: `{ticker}`")
    st.dataframe(df.tail())

    # Plotting basic line chart
    st.subheader("📊 Closing Price Chart")
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Close'])
    ax.set_xlabel("Date")
    ax.set_ylabel("Close Price")
    st.pyplot(fig)
