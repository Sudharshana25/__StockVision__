import yfinance as yf
import pandas as pd

def get_stock_data(ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
    data = yf.download(ticker, start=start_date, end=end_date)
    data.reset_index(inplace=True)
    return data

# Example usage
if __name__ == "__main__":
    df = get_stock_data("AAPL", "2023-01-01", "2023-12-31")
    print(df.head())
