__all__ = ['Stock']

from peewee import *
from .BaseModel import BaseModel

class Stock(BaseModel):
    symbol = CharField(unique=True)
    name = CharField()
