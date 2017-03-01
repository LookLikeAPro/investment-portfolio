from __future__ import unicode_literals
import datetime
import io
import pandas as pd

from src.datasource import get_stock
from src.transaction import Transaction

__all__ = ['Environment']

class DatedSeries:
  def __init__(self, dates=[], values=[]):
    self.dates = dates
    self.values = values
    self.last_access_id = 0
    self._df = pd.DataFrame({"value": []}, index=[])
  def insert(self, date, value):
    self.dates.append(date)
    self.values.append(value)
  @property
  def df(self):
    # self.value_over_time = self.value_over_time.append(new_value_df)
    if len(self.values) == self.last_access_id:
      return self._df
    self._df = pd.DataFrame({"value": self.values}, index=self.dates)
    self.last_access_id = len(self._df)
    return self._df

class Environment:
  def __init__(self):
    self.cash = float(1)
    self._date = datetime.datetime(2010, 1, 4)
    self.holdings = {}
    self.transactions = []
    self._value_over_time = DatedSeries()
  @property
  def date(self):
    return self._date
  @property
  def start_date(self):
    return self._start_date
  def _advance_date(self):
    self._date = self._date + datetime.timedelta(days=1)
    self.journal_value()
  def get_stock(self, symbol):
    stock = get_stock(symbol)
    return stock.ix[self.start_date:self.date]
  def get_stock_current_price(self, symbol):
    return self.get_stock(symbol)["Adj Close"][-1:][0]
  @property
  def value(self):
    total = self.cash
    for holding in self.holdings:
      stock_price = self.get_stock_current_price(holding)
      total += stock_price*self.holdings[holding]
    return total
  def journal_value(self):
    self._value_over_time.insert(self.date, self.value)
  @property
  def value_over_time(self):
    return self._value_over_time.df
  def buy(self, symbol, amount):
    stock_price = self.get_stock_current_price(symbol)
    if self.cash < amount:
      raise Exception('Not enough money!')
    self.holdings[symbol] = self.holdings.get(symbol, 0) + amount/stock_price
    self.cash -= amount
    self.transactions.append(Transaction("BUY", symbol, amount))
  def sell(self, symbol, amount):
    stock_price = self.get_stock_current_price(symbol)
    if stock_price*self.holdings.get(symbol, 0) < amount:
      raise Exception('Not enough holding of {}!'.format(symbol))
    self.holdings[symbol] = self.holdings[symbol] - amount/stock_price
    self.cash += amount
    self.transactions.append(Transaction("SELL", symbol, amount))
  def rebalance(self, weights):
    pass
  def __repr__(self):
    with io.StringIO() as output:
      output.write("Value: {}\n".format(self.value))
      output.write("Cash: {}\n".format(self.cash))
      output.write("Date: {}\n".format(self.date))
      output.write("Holdings:\n")
      for holding in self.holdings:
        output.write("{}: {}\n".format(holding, self.holdings[holding]))
      return output.getvalue()
