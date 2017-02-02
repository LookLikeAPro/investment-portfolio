def get_time_serialized(symbol):
  x = []
  y = []
  for i in Stock.get(Stock.symbol == symbol).prices:
    x.append(i.adj_close)
    y.append(i.date)
  return y, x

def graph_stock(symbols):
  import matplotlib.pyplot as plt
  for symbol in symbols:
    y, x = get_time_serialized(symbol)
    plt.plot(y, x)
  plt.ylabel('price')
  plt.show()

graph_stock(reit_symbols)
