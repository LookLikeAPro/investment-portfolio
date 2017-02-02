import sys
sys.path.append("..")
from src import startup

from src.datasource import get_stock
from src import constants

reit_symbols = constants.get_constant("canadian_reits")

for reit_symbol in reit_symbols:
  print("GET " + reit_symbol)
  get_stock(reit_symbol)
