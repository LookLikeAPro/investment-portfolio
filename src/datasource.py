import sys
import os
import pandas as pd
import datetime

def get_csv_path(symbol):
  BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  return os.path.join(BASE_DIR, "data", "stocks", symbol+".csv")

# import sqlalchemy
# db = sqlalchemy.create_engine('sqlite:///test.db')
# db.echo = False

def get_stock(symbol, **kwargs):
  # global db
  if "back_interval" in kwargs:
    start = datetime.date.today() - datetime.timedelta(days=kwargs["back_interval"])
    end = datetime.date.today()
  else:
    start = kwargs.get("start", datetime.datetime(1970,1,1))
    end = kwargs.get("end", datetime.date.today())
  try:
    # stock = pd.read_sql(table_name, db, index_col="Date")
    stock = pd.read_csv(get_csv_path(symbol), index_col='Date', parse_dates=True)
    return stock
  # except sqlalchemy.exc.OperationalError:
  except IOError:
    import pandas_datareader.data as web
    stock = web.DataReader(symbol, "yahoo", start, end)
    # stock.to_sql(table_name, db, if_exists="replace")
    stock.to_csv(get_csv_path(symbol))
    return stock

# TODO CONCATENATION AND UPDATE
# msft = msft.ix[datetime.datetime(2016,1,1):datetime.date.today()]
# msft1 = msft.ix[datetime.datetime(2016,1,1):datetime.datetime(2016,7,1)]
# msft2 = msft.ix[datetime.datetime(2016,4,1):datetime.date.today()]
# print msft.size
# print msft1.size
# print msft2.size
# print pd.concat([msft1, msft2]).drop_duplicates().reset_index(drop=True).size
# for i in goog.iterrows():
#   # print type(i)
#   print i[0]
#   print i[1]["Open"]
