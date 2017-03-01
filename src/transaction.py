import datetime

__all__ = ['Transaction']

class Transaction:
  def __init__(self, _type, symbol, amount):
    self.type = _type
    self.symbol = symbol
    self.amount = amount
  def __repr__(self):
    return "Transaction: {}, {}, {}".format(self.type, self.symbol, self.amount)
