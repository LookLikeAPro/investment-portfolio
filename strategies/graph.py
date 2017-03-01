import pandas as pd

def initialize(context, environment):
  pass

def rebalance(context, environment):
  pass

def end(context, environment):
  import matplotlib.pyplot as plt
  apple = environment.get_stock("D-UN.TO")
  combined = pd.DataFrame({"Adj Close": apple["Adj Close"], "Close": apple["Close"], "DIFF": apple["Close"] - apple["Adj Close"]})
  combined.plot()
  plt.show()
