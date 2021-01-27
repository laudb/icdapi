from flask import Blueprint, request,jsonify

records = Blueprint('records', '__name__')

from . import api