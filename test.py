from src.startup import *
# from yahoo_finance import Share
# from models import Stock, StockPrice
# from models.BaseModel import db

# db.create_tables([Stock, StockPrice])

# print(type(StockPrice.get(stock=1).date))

# import datetime
# import time
# '2016-04-08'
# print(time.strftime('%Y-%m-%d %H:%M:%S'))
# print(datetime.datetime.strptime('2016-04-08', "%Y-%m-%d"))
# print(datetime.date('2016-04-08'))

from src.datasource import get_stock

import pandas as pd
import datetime

start = datetime.datetime(2016,1,1)
end = datetime.date.today()

import matplotlib.pyplot as plt

apple = get_stock("AAPL")
# print apple
# print apple.columns
msft = get_stock("MSFT")
goog = get_stock("GOOG")

# print apple.head()

import matplotlib.pyplot as plt
msft = msft.ix[datetime.datetime(2016,1,1):datetime.date.today()]
goog = goog.ix[datetime.datetime(2016,1,1):datetime.date.today()]
apple = apple.ix[datetime.datetime(2016,1,1):datetime.date.today()]


# stocks = pd.DataFrame({"AAPL": apple["Adj Close"],
#                       "MSFT": msft["Adj Close"],
#                       "GOOG": goog["Adj Close"]})


# stocks.plot()
# stocks.plot(secondary_y = ["AAPL", "MSFT"], grid = True)


# stock_return = stocks.apply(lambda x: x / x[0])
# stock_return.plot(grid = True).axhline(y = 1, color = "black", lw = 2)

# import numpy as np
# stock_change = stocks.apply(lambda x: np.log(x) - np.log(x.shift(1))) # shift moves dates back by 1.
# stock_change.plot(grid = True).axhline(y = 0, color = "black", lw = 2)

# apple["Adj Close"].plot(grid = True)
# close_px = apple['Adj Close']
# close_px.plot(label='AAPL')
# mavg.plot(label='mavg')
# plt.legend()
# plt.show()
# print apple.columns
# print apple["Date"]
# print pd.to_datetime(apple["Date"])[0] == datetime.datetime(2016,1,4)
# print msft.columns
# msft.set_index('Date')
