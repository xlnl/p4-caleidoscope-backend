import models 

from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict

note = Blueprint('notes', 'note')

# model_to_dict(note) - is a function that will change our Model object (note) to a Dictionary class, /
# - We have to do this because we cannot jsonify something from a "Model" class, so in order to respond /
# to the client we must change our datatype from a Model Class to a Dictionary Class instance.
@note.route('/', methods=["GET"])
def get_all_notes():
    ## find the notes and change each one to a dictionary into a new array
    try:
        # query the DB to get all the dogs
        all_notes = models.Note.select()
        # parse the models into dictionary
        notes_to_dict = [model_to_dict(note) for note in all_notes]
        # shorter way => dogs = [model_to_dict(dog) for dog in models.Dog.select()]
        return jsonify(
            data=notes_to_dict, 
            status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(
            data={}, 
            status={"code": 401, "message": "Error getting the resources"})