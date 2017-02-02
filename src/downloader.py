from future.standard_library import hooks
with hooks():
  from urllib.request import urlopen, Request
import datetime
import csv
import io
from models import Stock, StockPrice

__all__ = ['get_historical']

def price_str_to_int(p):
  return int(float(p)*100)

def date_str_to_date(d):
  s = d.split('-')
  return datetime.date(int(s[0]), int(s[1]), int(s[2]))

def get_historical(stock_symbol):
  now = datetime.datetime.now()
  # url = f'http://chart.finance.yahoo.com/table.csv?s=aapl&a=5&b=18&c=2001&d=0&e=10&f=2017&g=d&ignore=.csv'
  url = 'http://chart.finance.yahoo.com/table.csv?s={}&a=1&b=1&c=1900&d={}&e={}&f={}&g=d&ignore=.csv'.format(stock_symbol, now.month-1, now.day, now.year)
  print(url)
  response = urlopen(url)
  data = response.read()
  csv_text = data.decode('utf-8')
  try:
    stock = Stock.create(name=stock_symbol, symbol=stock_symbol)
  except:
    stock = Stock.get(Stock.symbol == stock_symbol)
  with io.StringIO(csv_text) as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
        try:
          StockPrice.create(stock=stock,
            date=row["Date"],
            open=price_str_to_int(row["Open"]),
            high=price_str_to_int(row["High"]),
            low=price_str_to_int(row["Low"]),
            close=price_str_to_int(row["Close"]),
            volume=int(row["Volume"]),
            adj_close=price_str_to_int(row["Adj Close"]),
          )
        except:
          print("skip "+row["Date"])
