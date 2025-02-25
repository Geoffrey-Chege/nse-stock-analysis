# optimization_loop.py
import pandas as pd
from .moving_average_test import SmaCrossRiskManaged, run_backtest
from .utils import get_latest_file

def run_optimization(directory="data/raw", extension="csv"):
    # Dynamically load the latest CSV file
    csv_path = get_latest_file(directory, extension)
    data = pd.read_csv(csv_path, index_col="Date", parse_dates=True)

    # Define parameter pairs to test: (short_window, long_window)
    param_grid = [
        (10, 30),
        (20, 50),
        (30, 70)
    ]

    results_list = []

    for short, long in param_grid:
        print(f"\nTesting parameters: Short={short}, Long={long}")
        # Set the strategy's parameters
        SmaCrossRiskManaged.short_window = short
        SmaCrossRiskManaged.long_window = long
        results = run_backtest(data, cash=10000, commission=0.002)
        results_list.append((short, long, results['Return [%]']))
        print(results[['Return [%]', 'Max. Drawdown [%]', 'Sharpe Ratio']])

    print("\nSummary of Optimization Results:")
    for short, long, ret in results_list:
        print(f"Parameters (Short: {short}, Long: {long}) achieved Return: {ret:.2f}%")

if __name__ == "__main__":
    run_optimization()