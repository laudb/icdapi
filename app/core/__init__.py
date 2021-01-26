from flask import Blueprint, request

records = Blueprint('records', '__name__')

from . import api