import datetime

def initialize(context, environment):
  context.i = 1
  context.date = environment.date
  context.begin_date = environment.date

values = []
dates = []

def rebalance(context, environment):
  if context.date + datetime.timedelta(days=1) > environment.get_stock("AAPL").index[-1:][0]:
    return
  context.date = environment.date
  # print context
  print(
     str(environment.get_stock("AAPL").index[-1:][0]) + ": " + str(environment.get_stock("AAPL")["Adj Close"][-1:][0])
  )
  environment.buy("AAPL", 0.01)
  values.append(environment.value)
  dates.append(environment.date)

import pandas as pd

def end(context, environment):
  print environment
  apple = environment.get_stock("AAPL")
  apple_returns = apple["Adj Close"] / apple["Adj Close"][0]
  import matplotlib.pyplot as plt
  portfolio = pd.DataFrame({"value": values}, index=dates)
  combined = pd.DataFrame({"apple": portfolio["value"], "portfolio": apple_returns})
  combined.plot()
  plt.show()
