__all__ = ['StockPrice']

from peewee import *
from .BaseModel import BaseModel
from .Stock import Stock

class StockPrice(BaseModel):
    stock = ForeignKeyField(Stock, related_name='prices')
    date = DateField(formats=('%Y-%m-%d',))
    open = IntegerField()
    high = IntegerField()
    low = IntegerField()
    close = IntegerField()
    volume = BigIntegerField()
    adj_close = IntegerField()
    class Meta:
        primary_key = CompositeKey('stock', 'date')
        order_by = ('date',)
