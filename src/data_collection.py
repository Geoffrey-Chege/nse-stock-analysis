import yfinance as yf
import pandas as pd
from datetime import datetime

def fetch_and_save_data(ticker="AAPL", period="1y", folder_csv="data/raw/", folder_excel="data/raw/"):
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period)
    hist.index = hist.index.tz_localize(None)

    # Create a timestamp string, e.g., "20240305_1530"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Incorporate both the ticker and the timestamp into the filename
    csv_filename = f"{folder_csv}{ticker}_stock_data_{timestamp}.csv"
    excel_filename = f"{folder_excel}{ticker}_stock_data_{timestamp}.xlsx"

    hist.to_csv(csv_filename, index=True)
    hist.to_excel(excel_filename, index=True)

    print(f"Data saved to {csv_filename} and {excel_filename}")
    return hist

# Example usage:
#if __name__ == "__main__":
#    fetch_and_save_data(ticker="AAPL")