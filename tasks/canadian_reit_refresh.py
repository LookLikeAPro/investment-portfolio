import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src import startup
from src.datasource import get_stock
from src.constants import get_constant

reit_symbols = get_constant("canadian_reits")

for reit_symbol in reit_symbols:
  print("GET " + reit_symbol)
  get_stock(reit_symbol)
