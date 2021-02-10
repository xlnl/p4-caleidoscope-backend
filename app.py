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

############ vv "MIDDLEWARE" METHODS vv ##############

login_manager = LoginManager() # instantiating a new LoginManager in an app 
login_manager.init_app(app)

# middleware as concept -> flask way to connect db before request & close db after each request
# """Connect to the database before each request."""
@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()

# """Close the database connection after each request."""
@app.after_request
def after_request(response):
    g.db = models.DATABASE
    g.db.close()
    return response

CORS(app, origins=['http://localhost:3000'], supports_credentials=True) 

app.register_blueprint(note, url_prefix='/api/v1/note')
app.register_blueprint(person, url_prefix='/api/v1/users')
app.register_blueprint(user_note, url_prefix='/api/v1/user_note')
app.register_blueprint(user_event, url_prefix='/api/v1/user_event')
# express equivalent = app.use('/api/v1/note')

@app.route('/')
def index():
    return "landing stub"

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)