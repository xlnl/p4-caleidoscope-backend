from peewee import *
from flask_login import UserMixin

import datetime

DATABASE = PostgresqlDatabase('caleidoscope', host='localhost', port=5432)

class BaseModel(Model):
    class Meta: 
        database = DATABASE

class Person(UserMixin, BaseModel):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()
    city = CharField()
    zodiacSign = CharField()

class Note(BaseModel):
    block = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

class Event(BaseModel):
    title = CharField()
    startDate = DateField()
    endDate = DateField()
    startTime = TimeField()
    endTime = TimeField()
    location = CharField()
    description = TextField()


class PersonNote(BaseModel):
    person = ForeignKeyField(Person, backref='notes')
    note = ForeignKeyField(Note, backref='owner')

class PersonEvent(BaseModel):
    person = ForeignKeyField(Person, backref='events')
    event = ForeignKeyField(Event, backref='owner')

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Person, Note, Event, PersonNote, PersonEvent], safe=True) 
    print("Tables created!")
    DATABASE.close()