"""
Scalping Bot Agent (Core Logic)
--------------------------------
Strategy: EMA 9 / EMA 25 crossover
Timeframe: 5-minute candles
Market: Spot trading
NOTE: API keys are intentionally NOT included.
"""

import pandas as pd
import time


class ScalpingBot:
    def __init__(self, symbol, short_ema=9, long_ema=25):
        self.symbol = symbol
        self.short_ema = short_ema
        self.long_ema = long_ema
        self.position = None  # None, "BUY"

    def calculate_ema(self, data, period):
        return data['close'].ewm(span=period, adjust=False).mean()

    def generate_signal(self, df):
        df['ema_short'] = self.calculate_ema(df, self.short_ema)
        df['ema_long'] = self.calculate_ema(df, self.long_ema)

        if df['ema_short'].iloc[-2] < df['ema_long'].iloc[-2] and \
           df['ema_short'].iloc[-1] > df['ema_long'].iloc[-1]:
            return "BUY"

        if df['ema_short'].iloc[-2] > df['ema_long'].iloc[-2] and \
           df['ema_short'].iloc[-1] < df['ema_long'].iloc[-1]:
            return "SELL"

        return "HOLD"

    def execute_trade(self, signal):
        if signal == "BUY" and self.position is None:
            print(f"[TRADE] BUY order placed for {self.symbol}")
            self.position = "BUY"

        elif signal == "SELL" and self.position == "BUY":
            print(f"[TRADE] SELL order placed for {self.symbol}")
            self.position = None

        else:
            print("[INFO] No trade executed")

    def run(self, market_data):
        """
        market_data: pandas DataFrame with 'close' prices
        """
        signal = self.generate_signal(market_data)
        print(f"[SIGNAL] {signal}")
        self.execute_trade(signal)


# -------------------------------
# Example Usage (Simulation Mode)
# -------------------------------
if __name__ == "__main__":

    # Simulated price data (for testing without API)
    data = {
        "close": [
            100, 101, 102, 101, 103, 105, 107,
            106, 108, 110, 109, 111, 113, 112
        ]
    }

    df = pd.DataFrame(data)

    bot = ScalpingBot(symbol="BTC/USDT")
    bot.run(df)
