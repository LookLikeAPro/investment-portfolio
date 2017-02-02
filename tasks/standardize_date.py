import sys
sys.path.append("..")
from src import startup

from src.downloader import get_historical

get_historical("AAPL")
