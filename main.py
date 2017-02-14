import src.startup

from src.datasource import get_stock
from src.constants import get_constant

import matplotlib.pyplot as plt

import datetime

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


from src.environment import Environment

def import_strategy(strategy_name):
  from importlib import import_module
  try:
    strategy = import_module(strategy_name, __package__)
    return strategy
  except:
    raise("unable to load strategy")

class Context:
  pass

def simulate(strategy_name, **kwargs):
  start = kwargs.get("start", datetime.datetime(1970,1,1))
  end = kwargs.get("end", datetime.date.today())
  strat = import_strategy(strategy_name)
  context = Context()
  environment = Environment()
  environment._date = datetime.datetime(2016,7,1)
  strat.initialize(context, environment)
  for i in range(100):
    environment._advance_date()
    strat.rebalance(context, environment)
  strat.end(context, environment)

simulate("test1")