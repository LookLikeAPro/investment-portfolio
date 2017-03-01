import src.startup

from src.datasource import get_stock
from src.constants import get_constant

import matplotlib.pyplot as plt

import pandas as pd

# stocks = {}

# for symbol in ["D-UN.TO", "CUF-UN.TO", "RY"]:
#   stock = get_stock(symbol)[datetime.datetime(2016,1,1):datetime.date.today()]
#   # stock["LMA"] = stock["Adj Close"].rolling(window=20).mean()
#   # stock["LMA"].plot()
#   stock["returns"] = stock["Adj Close"] / stock["Adj Close"][0]
#   # stock["returns"].plot(label= symbol)
#   stocks[symbol] = stock["returns"]

# stocks = pd.DataFrame(stocks)
# stocks.plot()
# plt.show()

from src.simulator import simulate

simulate("strategies.graph")
