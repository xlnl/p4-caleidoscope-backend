from flask import Flask, render_template, g
from flask_cors import CORS
from flask_login import LoginManager

import models
from models import Person
from resources.users import person
from resources.notes import note
from resources.events import event


DEBUG = True
PORT = 8000

app = Flask(__name__)

app.config.from_pyfile('config.py')

############ vv "MIDDLEWARE" METHODS vv ##############

login_manager = LoginManager() # instantiating a new LoginManager in an app 
login_manager.init_app(app)

# callback for user_loader per flask auth docs; this will be called everytime a request comes from the server
# loads the user from the user id stored in the session cookie
@login_manager.user_loader
def load_user(person_id):
    try:
        print(person_id)
        return Person.get(int(person_id))
    except models.DoesNotExist:
        return None 

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

app.register_blueprint(person, url_prefix='/api/v1/user')
app.register_blueprint(note, url_prefix='/api/v1/note')
app.register_blueprint(event, url_prefix='/api/v1/event')
# express equivalent = app.use('/api/v1/note')

@app.route('/')
def index():
    return "landing stub"

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)