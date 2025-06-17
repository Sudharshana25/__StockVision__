import yfinance as yf
import pandas as pd

def get_stock_data(ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
    data = yf.download(ticker, start=start_date, end=end_date)
    data.reset_index(inplace=True)
    return data
def add_moving_averages(df, windows=[20, 50]):
    for window in windows:
        df[f'SMA_{window}'] = df['Close'].rolling(window=window).mean()
    return df
def add_rsi(df, period=14):
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    return df

# Example usage
if __name__ == "__main__":
    df = get_stock_data("AAPL", "2023-01-01", "2023-12-31")
    print(df.head())
