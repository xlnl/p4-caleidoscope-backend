from flask import Flask, render_template, g
from flask_cors import CORS
from flask_login import LoginManager

import models
from resources.users import person
from resources.user_notes import user_note
from resources.user_events import user_event
from resources.notes import note
from resources.events import event

DEBUG = True
PORT = 8000

app = Flask(__name__)

app.config.from_pyfile('config.py')

@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    g.db = models.DATABASE
    g.db.close()
    return response

CORS(app, origins=['http://localhost:3000'], supports_credentials=True) 

@app.route('/')
def index():
    return "landing stub"

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)