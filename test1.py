import datetime

def initialize(context, environment):
  context.i = 1
  context.date = environment.date

def rebalance(context, environment):
  if context.date + datetime.timedelta(days=1) >= environment.get_stock("AAPL").index[-1:][0]:
    return
  context.date = environment.date
  # print context
  print "today: " + str(environment.get_stock("AAPL")["Open"][-1:])
  environment.buy("AAPL", 0.01)
  # import matplotlib.pyplot as plt
  # environment.get_stock("AAPL")["Open"].plot()
  # plt.show()

def end(context, environment):
  print environment
