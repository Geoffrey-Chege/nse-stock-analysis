# main.py
from src.data_collection import fetch_and_save_data
from src.EDA_historical import load_data, perform_eda
from src.moving_average_test import run_backtest
from src.optimization_loop import run_optimization

def main():
    # Step 1: Fetch and save data from Yahoo Finance.
    # (This will save the data to a file with a unique timestamp and ticker in the name.)
    # You can comment this out if you already have saved data.
    fetch_and_save_data(ticker="AAPL", period="1y")

    # Step 2: Load the saved data.
    df = load_data(directory="data/raw", extension="csv")

    # Step 3: Perform exploratory data analysis.
    perform_eda(df)

    # Step 4: Run the backtest with the current strategy.
    run_backtest(df)

    # Step 5: Run optimization over a range of parameter values.
    run_optimization(directory="data/raw", extension="csv")

if __name__ == "__main__":
    main()