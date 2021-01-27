from flask import request,jsonify
from . import records

from app.models import Record


@records.route("/status", methods=["GET"])
def status():
    return f"diagnose api: Version 1"

@records.route("/records", methods=["GET"])
def show_all():
    records = Record.query.all()
    return records

@records.route("/records", methods=["POST"])
def create():
    payload = request.get_json()
    result = Record(payload)
    result = result.save()
    return str(result)

@records.route("/records/<int: id>", methods=["PUT"])
def edit_one(id):
    pass

@records.route("/records/<int: id>", methods=["GET"])
def get_one(id):
    record = Record.query.get_or_404(id)

@records.route("/records/<int: id>", methods=["DELETE"])
def delete_one(id):
    pass

