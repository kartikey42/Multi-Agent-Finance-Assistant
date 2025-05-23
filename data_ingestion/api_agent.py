# -----------------------------
import yfinance as yf

def get_asia_tech_data():
    tickers = ['TSM', 'SSNLF']  # TSMC, Samsung
    data = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="2d")
        if not hist.empty:
            data[ticker] = {
                'price_change': (hist['Close'][-1] - hist['Close'][-2]) / hist['Close'][-2] * 100
            }
    return data
