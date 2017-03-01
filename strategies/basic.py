import datetime

def initialize(context, environment):
  context.i = 1
  context.date = environment.date
  context.begin_date = environment.date

stock = "D-UN.TO"

def rebalance(context, environment):
  if not len(environment.get_stock(stock)):
    return
  if context.date + datetime.timedelta(days=1) > environment.get_stock(stock).index[-1:][0]:
    return
  context.date = environment.date
  print(
     str(environment.get_stock(stock).index[-1:][0]) + ": " + str(environment.get_stock(stock)["Close"][-1:][0])
  )
  environment.buy(stock, 0.005)

import pandas as pd

def end(context, environment):
  print environment
  # print environment.transactions
  apple = environment.get_stock(stock)
  apple_returns = apple["Adj Close"] / apple["Adj Close"][0]
  import matplotlib.pyplot as plt
  x = environment.value_over_time
  y = x.index.intersection(apple.index)
  z = x.ix[y]
  combined = pd.DataFrame({"value": z["value"], "stock": apple_returns})
  combined.plot()
  plt.show()
