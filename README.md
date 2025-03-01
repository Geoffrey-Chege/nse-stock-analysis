# NSE Stock Analysis & Backtesting

## Overview
This project is designed to fetch historical stock data from Yahoo Finance, perform exploratory data analysis (EDA), backtest a moving-average crossover trading strategy, and optimize strategy parameters. It provides a modular framework that can be further expanded to include risk management, alternative strategies, and additional data sources for paper or live trading.

## Features
- **Data Collection:**  
  Fetches historical stock data using yfinance and saves it with unique filenames (including ticker and timestamp).
- **Exploratory Data Analysis (EDA):**  
  Loads saved data, displays summary statistics, and visualizes key trends such as closing prices.
- **Backtesting:**  
  Implements a moving average crossover strategy using the backtesting library and outputs performance metrics like Return, Max Drawdown, and Sharpe Ratio.
- **Optimization:**  
  Tests different parameter combinations to determine the optimal strategy settings.
- **Modular Structure:**  
  Organized into separate modules for data collection, EDA, strategy, backtesting, and optimization for easy maintenance and future enhancements.

## Project Structure
```
nse-stock-analysis/ 
├── data/ 
│ ├── raw/ # Raw data files downloaded from Yahoo Finance 
│ └── processed/ # Processed data files (if applicable) 
├── src/ 
│ ├── init.py # Marks the src folder as a Python package 
│ ├── data_collection.py # Module for fetching and saving data from Yahoo Finance 
│ ├── EDA_historical.py # Module for loading data and performing EDA 
│ ├── moving_average_test.py # Module for the moving average crossover strategy and backtesting 
│ ├── optimization_loop.py # Module for optimizing strategy parameters 
│ └── utils.py # Helper functions (e.g., get_latest_file) 
├── main.py # Entry point tying all modules together 
├── requirements.txt # List of project dependencies 
└── README.md # This file
```

## Installation

1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd nse-stock-analysis
   ```
   
2. **Set Up the Virtual Environment:**
   ```bash
   python -m venv venv
   ```
   Activate the virtual environment:
   
   - On Windows(PowerShell):
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
   
   - On Windows (CMD):
   ```cmd
   .\venv\Scripts\activate
   ```
   
   - On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   
## Usage

Run the main script to execute the full workflow:
```bash
python main.py
```
This will:

- Fetch and save historical stock data (with unique filenames) into the data/raw/ folder.
- Load the latest data file dynamically and perform exploratory data analysis.
- Backtest the moving average crossover strategy.
- Run an optimization loop over different strategy parameters.

## Customization
- Ticker & Period:
  Change the ticker symbol and period in the call to fetch_and_save_data in main.py.

- Strategy Parameters:
  Adjust the short_window and long_window in moving_average_test.py or modify the parameter grid in optimization_loop.py.

- Risk Management:
  The current strategy includes basic stop-loss and take-profit rules. These can be refined in moving_average_test.py.

## Future Enhancements
- Add more technical indicators (RSI, MACD, Bollinger Bands) to refine trade signals.
- Incorporate advanced risk management techniques and position sizing.
- Develop an interactive dashboard using Streamlit or Dash.
- Explore alternative trading strategies and machine learning models for forecasting.
- Transition from backtesting to paper trading or live trading once the strategy is robust.

## License
This project is licensed under the MIT License.

Contributing
Contributions are welcome! Please fork the repository and submit pull requests. For issues or suggestions, open an issue in the repository.

Contact
For questions or further assistance, please contact Geoffrey Chege Mwangi at geoffrey.c.chege@gmail.com.
   
   
