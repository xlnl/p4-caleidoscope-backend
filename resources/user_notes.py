import models 

from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict

user_note = Blueprint('user_notes', 'user_note')