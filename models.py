from peewee import *
from flask_login import UserMixin, LoginManager
import os
from playhouse.db_url import connect

import datetime

DATABASE = PostgresqlDatabase('caleidoscope', host='localhost', port=5432)
# DATABASE = connect(os.environ.get('DATABASE_URL'))

class BaseModel(Model):
    class Meta: 
        database = DATABASE
    
class Person(UserMixin, BaseModel):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()
    city = CharField()
    country = CharField()
    zodiacSign = CharField()

class Note(BaseModel):
    block = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)
    person = ForeignKeyField(Person, backref='notes')

class Event(BaseModel):
    title = CharField()
    startDate = DateField()
    endDate = DateField()
    startTime = TimeField()
    endTime = TimeField()
    location = CharField()
    description = TextField()
    person = ForeignKeyField(Person, backref='events')

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Person, Note, Event]) 
    print("Tables created!")
    DATABASE.close()