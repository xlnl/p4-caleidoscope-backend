import models 

from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict

person = Blueprint('persons', 'person')