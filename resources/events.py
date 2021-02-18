import models 

from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

event = Blueprint('events', 'event')

# model_to_dict(event) - is a function that will change our Model object (event) to a Dictionary class, /
# - We have to do this because we cannot jsonify something from a "Model" class, so in order to respond /
# to the client we must change our datatype from a Model Class to a Dictionary Class instance.
@event.route('/', methods=["GET"])
# debug with create route to ensure timecode gets deserialize 
## https://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable
@login_required
def get_all_events():
    try:
        all_events = models.Event.select()
        events_to_dict = [model_to_dict(event) for event in all_events]
        return jsonify(
            data=events_to_dict, 
            status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(
            data={}, 
            status={"code": 401, "message": "Error getting the resources"})

@event.route('/', methods=["POST"])
# figure out debugging this to deserialize timecodes for JSON 
@login_required
def create_event():
    ## see request payload anagolous to req.body in express
    payload = request.get_json()
    event = models.Event.create(**payload)
    event_dict = model_to_dict(event)
    return jsonify(data=event_dict, status={"code": 201, "message": "Success"})

@event.route('/<event_id>', methods=["GET"])
@login_required
def get_event(event_id):
    try:
        event = models.Event.get_by_id(event_id)
        event_dict = model_to_dict(event)
        return jsonify(
            data=event_dict, 
            status={"code": 201, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(
            data={}, 
            status={"code": 401, "message": "Error getting the resources"})

@event.route('/<event_id>/update', methods=["PUT"])
@login_required
def update_event(event_id):
    try:
        payload = request.get_json()
        query = models.Event.update(**payload).where(models.Event.id==event_id)
        query.execute()
        updated_event = model_to_dict(models.Event.get_by_id(event_id))
        return jsonify(
            data=updated_event, 
            status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(
            data={}, 
            status={"code": 401, "message": "Error getting the resources"})

@event.route('/<event_id>', methods=["Delete"])
@login_required
def delete_event(event_id):
    try: 
        event_to_delete = models.Event.get_by_id(event_id)
        event_to_delete.delete_instance()
        return jsonify(
            data={}, 
            status={"code": 200, "message": "Success, resources successfully delete"})
    except models.DoesNotExist:
        return jsonify(
            data={}, 
            status={"code": 401, "message": "Error getting the resources"})