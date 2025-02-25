# moving_average_test.py
from backtesting import Backtest, Strategy
import pandas as pd

'''
class SmaCross(Strategy):
    # Default parameters – these can be adjusted or optimized later
    short_window = 20
    long_window  = 50

    def init(self):
        # Use self.I() to register our indicator calculations
        self.ma_short = self.I(lambda: pd.Series(self.data.Close).rolling(self.short_window).mean())
        self.ma_long  = self.I(lambda: pd.Series(self.data.Close).rolling(self.long_window).mean())

    def next(self):
        # Buy signal: when short MA crosses above long MA
        if not self.position:
            if self.ma_short[-1] > self.ma_long[-1] and self.ma_short[-2] <= self.ma_long[-2]:
                self.buy()
        # Sell signal: when short MA crosses below long MA
        elif self.ma_short[-1] < self.ma_long[-1] and self.ma_short[-2] >= self.ma_long[-2]:
            self.position.close()
'''

'''
class SmaCrossRiskManaged(Strategy):
    # Default parameters – these can be adjusted or optimized later
    short_window = 20
    long_window  = 50
    # Define risk management parameters
    stop_loss_pct = 0.05    # 5% stop-loss
    take_profit_pct = 0.10  # 10% take-profit

    def init(self):
        # Use self.I() to register our indicator calculations
        self.ma_short = self.I(lambda: pd.Series(self.data.Close).rolling(self.short_window).mean())
        self.ma_long  = self.I(lambda: pd.Series(self.data.Close).rolling(self.long_window).mean())

    def next(self):
        # Entry condition: short MA crosses above long MA
        if not self.position:
            if self.ma_short[-1] > self.ma_long[-1] and self.ma_short[-2] <= self.ma_long[-2]:
                self.buy()
        else:
            # Check for stop-loss and take-profit conditions
            current_price = self.data.Close[-1]
            entry_price = self.position.entry_price

            if current_price <= entry_price * (1 - self.stop_loss_pct):
                self.position.close()  # Trigger stop-loss
            elif current_price >= entry_price * (1 + self.take_profit_pct):
                self.position.close()  # Trigger take-profit
            # Additionally, exit if MA crossover signal reverses
            elif self.ma_short[-1] < self.ma_long[-1] and self.ma_short[-2] >= self.ma_long[-2]:
                self.position.close()
'''

class SmaCrossRiskManaged(Strategy):
    short_window = 20
    long_window  = 50
    stop_loss_pct = 0.05    # 5% stop-loss
    take_profit_pct = 0.10  # 10% take-profit

    def init(self):
        # Register the moving average indicators
        self.ma_short = self.I(lambda: pd.Series(self.data.Close).rolling(self.short_window).mean())
        self.ma_long  = self.I(lambda: pd.Series(self.data.Close).rolling(self.long_window).mean())
        # We'll store the entry price manually when we open a position
        self.entry_price = None

    def next(self):
        # If not in a position, look for an entry signal
        if not self.position:
            if self.ma_short[-1] > self.ma_long[-1] and self.ma_short[-2] <= self.ma_long[-2]:
                self.buy()
                # Record the entry price manually
                self.entry_price = self.data.Close[-1]
        else:
            # If in a position, use our stored entry price to check risk management rules
            current_price = self.data.Close[-1]
            if self.entry_price is not None:
                # Check stop-loss condition
                if current_price <= self.entry_price * (1 - self.stop_loss_pct):
                    self.position.close()  # Trigger stop-loss
                    self.entry_price = None  # Reset entry price after exit
                # Check take-profit condition
                elif current_price >= self.entry_price * (1 + self.take_profit_pct):
                    self.position.close()  # Trigger take-profit
                    self.entry_price = None  # Reset entry price after exit
                # Check for a moving average crossover exit signal
                elif self.ma_short[-1] < self.ma_long[-1] and self.ma_short[-2] >= self.ma_long[-2]:
                    self.position.close()  # Exit based on signal
                    self.entry_price = None  # Reset entry price

def run_backtest(data, cash=10000, commission=0.002):
    """
    Run the backtest on the given data using the SmaCross strategy.
    """
    bt = Backtest(data, SmaCrossRiskManaged, cash=cash, commission=commission)
    results = bt.run()
    print(results[['Return [%]', 'Max. Drawdown [%]', 'Sharpe Ratio']])
    bt.plot()
    return results