# EDA_historical.py
import pandas as pd
import matplotlib.pyplot as plt
from .utils import get_latest_file  # assuming you place the helper function in utils.py

#def load_data(csv_path="data/raw/nse_stock_data.csv"):
#    """
#    Load historical stock data from a CSV file.
#    """
#    df = pd.read_csv(csv_path, index_col="Date", parse_dates=True)
#    return df

def load_data(directory="data/raw", extension="csv"):
    # Dynamically determine the latest CSV file in the specified directory
    csv_path = get_latest_file(directory, extension)
    df = pd.read_csv(csv_path, index_col="Date", parse_dates=True)
    print(f"Loaded data from {csv_path}")
    return df

def perform_eda(df):
    """
    Perform exploratory data analysis on the DataFrame.
    """
    print("Data Information:")
    print(df.info())
    print("\nFirst 5 Rows:")
    print(df.head())

    # Plot the closing price over time
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df['Close'], label='Close Price')
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title("Closing Price Over Time")
    plt.legend()
    plt.show()
