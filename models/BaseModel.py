__all__ = ['BaseModel', 'db']

from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase
import datetime


import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db = SqliteExtDatabase(os.path.join(BASE_DIR, "data", "main.db"))

class BaseModel(Model):
    class Meta:
        database = db

db.connect()
