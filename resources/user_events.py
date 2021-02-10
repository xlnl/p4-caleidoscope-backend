import models 

from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict

user_event = Blueprint('user_events', 'user_event')