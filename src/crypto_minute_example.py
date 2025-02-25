import ccxt
import pandas as pd
import matplotlib.pyplot as plt

# Create an instance of the Binance exchange
exchange = ccxt.binance({
    'enableRateLimit': True,  # Always use rate limiting to avoid bans
})

# Define the market symbol (for example, Bitcoin against USDT)
symbol = 'BTC/USDT'

# Define the timeframe (e.g., '1m' for 1-minute candles)
timeframe = '1m'

# Define how many candles you want (e.g., 60 for the past hour if 1-minute candles)
limit = 60

# Fetch the OHLCV data
ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)

# Convert to a Pandas DataFrame
df = pd.DataFrame(ohlcv, columns=['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume'])
df['Date'] = pd.to_datetime(df['Timestamp'], unit='ms')
df.set_index('Date', inplace=True)
df.drop('Timestamp', axis=1, inplace=True)

# Save the Binance BTC/USDT 1-minute candle data to a CSV file
df.to_csv("binance_btc_usdt_1m.csv", index=True)

# Save the data to an Excel file (requires 'openpyxl' – install via pip if needed)
df.to_excel("binance_btc_usdt_1m.xlsx", index=True)


print(df.head())

# Plot the closing prices
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['Close'], label='Close Price')
plt.xlabel("Time")
plt.ylabel("Price (USDT)")
plt.title("BTC/USDT 1-Minute Candle Data")
plt.legend()
plt.show()
