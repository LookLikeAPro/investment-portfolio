from models import Stock, StockPrice

def is_trade_day(date):
  staple_stock = Stock.get(Stock.symbol == "AAPL")
  return StockPrice.filter(StockPrice.stock == staple_stock, StockPrice.date == date).count() > 0

from datetime import timedelta

def next_trade_day(date):
  for i in range(10):
    if is_trade_day(date):
      return date
    date += timedelta(days=1)
  raise Exception("No next trade day")
