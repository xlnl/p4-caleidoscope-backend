import models

from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user

person = Blueprint('persons', 'person')

@person.route('/register', methods=["POST"])
def register():
    ## see request payload anagolous to req.body in express
    payload = request.get_json()
    payload['email'].lower()
    payload['username'].lower()
    
    try:
        # does the user already exist/is the username taken?
        models.Person.get(models.Person.email == payload['email'])
        return jsonify(
            data={}, 
            status={"code": 401, 
                    "message": "A user with that email already exists"})
    except models.DoesNotExist:
        # if user doesn't exist, create user and bcrypt password
        payload['password'] = generate_password_hash(payload['password'])
        Person = models.Person.create(**payload)
        
        login_user(person)

        person_dict = model_to_dict(person)

        del person_dict['password'] # don't expose password!
        
        return jsonify(
            data=person_dict, 
            status={"code": 201, "message": "Success! Created user"})

@person.route('/login', methods=["POST"])
def login():
    payload = request.get_json()
    payload['username'].lower()

    try:
        person = models.Person.get(models.Person.username == payload['username'])

        person_dict = model_to_dict(person)

        # check_password_hash(hashed_pw_from_db, unhashed_pw_from_payload)
        if(check_password_hash(person_dict['password'], payload['password'])):
            del person_dict['password']
            login_user(person)
            return jsonify(
                data=person_dict,
                status={"code": 201, "message": "Success! Logged in user"})
        else:
            return jsonify(
                data={}, 
                status={"code": 401, 
                        "message": "Can't log in user - password or username is incorrect"})
    except models.DoesNotExist:
        return jsonify(
            data={}, 
            status={"code": 401, 
                    "message": "Can't log in user - password or username is incorrect"})

@person.route('/logout', methods=["GET", "POST"])
def logout():
    if current_user:
        logout_user()
        return jsonify(
            data={},
            status={"code": 200, "message": "Success! Logged out user"})
    else:
        return jsonify(
            data={},
            status={"code": 401, "message": "You are not logged in."})