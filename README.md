# __StockVision__


**StockVision** is a real-time stock analytics and prediction platform that leverages machine learning to analyze stock market data and visualize key indicators like candlestick charts, RSI, MACD, and more.

---

##  Features

-  Real-time candlestick chart visualization
-  Technical indicators: RSI, MACD, SMA, EMA
-  ML-based stock prediction (LSTM, Linear Regression, ARIMA)
-  Interactive Streamlit dashboard
-  User-friendly interface for traders, analysts, and students

---

## 🛠 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python (Pandas, NumPy, Scikit-learn, Keras, statsmodels)
- **Visualization**: Plotly, Matplotlib
- **Modeling**: LSTM, ARIMA, Linear Regression
- **Deployment**: Streamlit Cloud

---

##  Project Structure
StockVision/
├── dashboard/
│ └── app.py # Streamlit app entry point
├── models/
│ ├── lstm_model.pkl
│ └── linear_model.pkl
├── data/
│ └── sample_data.csv
├── requirements.txt
└── README.md


---

##  Run Locally

```bash
git clone https://github.com/Sudharshana25/__StockVision__.git
cd __StockVision__/dashboard
pip install -r ../requirements.txt
streamlit run app.py

