from flask import request, jsonify
from app import db
from . import records

from app.models import Record


@records.route("/status", methods=["GET"])
def status():
    return f"diagnose api: Version 1"

@records.route("/records/page/<int:id>", methods=["GET"])
def show_all(page=1):
    batch = 20
    records = Record.query.order_by(
        Record.code.desc()
    ).paginate(page, per_page=batch)
    return records

@records.route("/records", methods=["POST"])
def create():
    payload = request.get_json()
    result = Record(payload) # validate respective sections on input before saving
    result = result.save()
    return str(result)

@records.route("/records/<int:id>", methods=["PUT"])
def edit_one(id):
    record = Record.query.get_or_404(id)
    data = request.get_json()
    for one in data:
        record[one] = data[one] 
    result = record.save()
    return result

@records.route("/records/<int:id>", methods=["GET"])
def get_one(id):
    record = Record.query.get_or_404(id)
    return record

@records.route("/records/<int:id>", methods=["DELETE"])
def delete_one(id):
    record = Record.query.get_or_404(id)
    record.delete()
    return id

