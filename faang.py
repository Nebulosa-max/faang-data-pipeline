import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os
import glob


def get_data():
    tickers = ["META", "AAPL", "AMZN", "NFLX", "GOOG"]

    data = yf.download(
        tickers,
        period="5d",
        interval="1h"
    )

    if not os.path.exists("data"):
        os.makedirs("data")

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"data/{timestamp}.csv"

    data.to_csv(filename)
    print(f"Data saved to {filename}")


def plot_data():
    files = glob.glob("data/*.csv")
    latest_file = max(files)

    data = pd.read_csv(latest_file, header=[0,1], index_col=0)
    close_data = data["Close"]

    plt.figure(figsize=(10,6))

    for ticker in close_data.columns:
        plt.plot(close_data.index, close_data[ticker], label=ticker)

    plt.title("FAANG Stock Prices (Last 5 Days)")
    plt.xlabel("Time")
    plt.ylabel("Price (USD)")
    plt.legend()

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"plots/{timestamp}.png"

    plt.savefig(filename)
    print(f"Plot saved to {filename}")


if __name__ == "__main__":
    get_data()
    plot_data()
