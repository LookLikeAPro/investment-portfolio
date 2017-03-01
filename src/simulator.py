import datetime

from src.environment import Environment

__all__ = ['simulate']

class Context:
  pass

def import_strategy(strategy_name):
  from importlib import import_module
  try:
    strategy = import_module(strategy_name, __package__)
    return strategy
  except:
    raise("unable to load strategy")

def simulate(strategy_name, **kwargs):
  start = kwargs.get("start", datetime.datetime(1970,1,1))
  end = kwargs.get("end", datetime.date.today())
  strat = import_strategy(strategy_name)
  context = Context()
  environment = Environment()
  environment._date = datetime.datetime(2016,7,1)
  environment._start_date = datetime.datetime(2016,7,1)
  strat.initialize(context, environment)
  for i in range(200):
    environment._advance_date()
    strat.rebalance(context, environment)
  strat.end(context, environment)
