from __future__ import unicode_literals
from datetime import date
import io

__all__ = ['Portfolio']

from models import Stock, StockPrice

class Transaction:
  def __init__(self, type, stock, amount):
    self.type = type
    self.stock = stock
    self.amount = amount

def get_stock_price(symbol, date):
  stock = Stock.get(Stock.symbol == symbol)
  stock_price = StockPrice.get(StockPrice.stock == stock, StockPrice.date == date)
  return stock_price

class Portfolio:
  def __init__(self):
    self.cash = float(1)
    self.date = date(2010, 1, 4)
    self.holdings = {}
    self.transactions = []
  @property
  def value(self):
    total = self.cash
    for holding in self.holdings:
      stock_price = get_stock_price(holding, self.date)
      total += stock_price.open*self.holdings[holding]
    return total
  def buy(self, symbol, amount):
    stock_price = get_stock_price(symbol, self.date)
    if self.cash < amount:
      raise Exception('Not enough money!')
    self.holdings[symbol] = self.holdings.get(symbol, 0) + amount/stock_price.open
    self.cash -= amount
    self.transactions.append(Transaction("BUY", symbol, amount))
  def sell(self, symbol, amount):
    stock_price = get_stock_price(symbol, self.date)
    if stock_price.open*self.holdings.get(symbol, 0) < amount:
      raise Exception('Not enough holding of {}!'.format(symbol))
    self.holdings[symbol] = self.holdings[symbol] - amount/stock_price.open
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
