from flask import Flask, render_template, g, session, make_response
from flask_cors import CORS
from flask_login import LoginManager

import os
from playhouse.db_url import connect

import models
from models import Person
from resources.users import person
from resources.notes import note
from resources.events import event


DEBUG = True
PORT = 8000

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hewwohingadingadergen'
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
    app.config.update(SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=True)
    g.db = models.DATABASE
    g.db.connect()

# """Close the database connection after each request."""
@app.after_request
def after_request(response):
    app.config.update(SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=True)
    response.headers.add("Set-Cookie", f"my_cookie='a cookie'; Secure; SameSite=None;")
    g.db = models.DATABASE
    g.db.close()
    return response

@app.route('/')
def hello_world():
    resp = make_response("Hello, World!")
    return "Hello, this flask app is working!!!"

CORS(app, origins=['http://localhost:3000','https://caleidscope-api.herokuapp.com','https://caleidoscope.herokuapp.com'], supports_credentials=True) 

app.register_blueprint(person, url_prefix='/api/v1/user')
app.register_blueprint(note, url_prefix='/api/v1/note')
app.register_blueprint(event, url_prefix='/api/v1/event')
# express equivalent = app.use('/api/v1/note')
CORS(user)
CORS(note)
CORS(event)


if 'ON_HEROKU' in os.environ:
    print('hitting ')
    models.initialize()

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)