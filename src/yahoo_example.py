import yfinance as yf
import matplotlib.pyplot as plt

# Define the stock ticker. For example, Apple Inc.
ticker_symbol = "AAPL"

# Create a Ticker object for the given symbol
stock = yf.Ticker(ticker_symbol)

# Retrieve historical market data for the past year
hist = stock.history(period="1y")

hist.index = hist.index.tz_localize(None)
hist.to_excel("nse_stock_data.xlsx", index=True)

# Save the historical data to a CSV file
#hist.to_csv("nse_stock_data.csv", index=True)

# Save the historical data to an Excel file
#hist.to_excel("nse_stock_data.xlsx", index=True)


# Display the first few rows of the data
print(hist.head())

# Plot the closing prices over time
plt.figure(figsize=(10, 5))
plt.plot(hist.index, hist['Close'], label='Close Price')
plt.title(f"{ticker_symbol} Stock Price (Last 1 Year)")
plt.xlabel("Date")
plt.ylabel("Closing Price (USD)")
plt.legend()
plt.show()