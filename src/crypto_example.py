from pycoingecko import CoinGeckoAPI
import pandas as pd
import matplotlib.pyplot as plt

# Initialize the CoinGecko API client
cg = CoinGeckoAPI()

# Fetch the market chart data for Bitcoin in USD for the past 30 days
data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)

# The API returns data with keys like 'prices', 'market_caps', 'total_volumes'
# We'll work with 'prices' which is a list of [timestamp, price] pairs.
df = pd.DataFrame(data['prices'], columns=['Timestamp', 'Price'])

# Convert the timestamp (in milliseconds) to a readable date format
df['Date'] = pd.to_datetime(df['Timestamp'], unit='ms')
df.set_index('Date', inplace=True)
df.drop('Timestamp', axis=1, inplace=True)

# Print the first few rows to verify the data
print(df.head())

# Plot the price data
plt.figure(figsize=(10,6))
plt.plot(df.index, df['Price'], label='Bitcoin Price (USD)')
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.title("Bitcoin Price Over the Last 30 Days")
plt.legend()
plt.show()
