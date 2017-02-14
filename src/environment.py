from __future__ import unicode_literals
import datetime
import io

from src.datasource import get_stock

__all__ = ['Environment']

class Environment:
  def __init__(self):
    self.cash = float(1)
    self._date = datetime.datetime(2010, 1, 4)
    self.holdings = {}
    self.transactions = []
  @property
  def date(self):
    return self._date
  @property
  def start_date(self):
    return self._start_date
  def _advance_date(self):
    self._date = self._date + datetime.timedelta(days=1)
  def get_stock(self, symbol):
    stock = get_stock(symbol)
    return stock.ix[self.start_date:self.date]
  @property
  def value(self):
    total = self.cash
    for holding in self.holdings:
      stock_price = self.get_stock(holding)["Adj Close"][-1:][0]
      total += stock_price*self.holdings[holding]
    return total
  def buy(self, symbol, amount):
    stock_price = self.get_stock(symbol)["Adj Close"][-1:][0]
    if self.cash < amount:
      raise Exception('Not enough money!')
    self.holdings[symbol] = self.holdings.get(symbol, 0) + amount/stock_price
    self.cash -= amount
    # self.transactions.append(Transaction("BUY", symbol, amount))
  def sell(self, symbol, amount):
    stock_price = self.get_stock(symbol)["Adj Close"][-1:][0]
    if stock_price*self.holdings.get(symbol, 0) < amount:
      raise Exception('Not enough holding of {}!'.format(symbol))
    self.holdings[symbol] = self.holdings[symbol] - amount/stock_price
    self.cash += amount
    # self.transactions.append(Transaction("SELL", symbol, amount))
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
