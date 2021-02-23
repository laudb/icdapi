from flask import request, jsonify
from app import db
from . import records

from app.models import Record

@records.route("/status", methods=["GET"])
def status():
    return f"diagnose api: Version 1", 200

@records.route("/records/page/<int:page_id>", methods=["GET"])
def show_all(page_id=1):
    
    batch = 20
    pagination = Record.query.order_by(Record.code.desc()).paginate(page_id, per_page=batch)
    records = pagination.items
    
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_posts', page=page-1)
    
    next = None
    if pagination.has_next:
        next = url_for('api.get_posts', page=page+1)

    return jsonify({
        'records':[record.serialise() for record in records],
        'previous_url': prev,
        'next_url': next,
        'count': pagination.total
    }), 200

@records.route("/records", methods=["POST"])
def create():
    payload = request.get_json()
    valid = Record.is_icd_valid(payload['code'])
    if not valid:
        return jsonify({ 'message': 'Invalid input' }), 400
    result = Record(
        code=payload['code'], desc_short=payload['desc_short'], desc_long=payload['desc_long'],
        type=payload['type'], year=payload['year']
    )
    result = result.save()
    return jsonify({ 'status': 'created' }), 201

@records.route("/records/<int:id>", methods=["PUT"])
def edit_one(id):
    record = Record.query.get_or_404(id)
    data = request.get_json()
    for one in data:
        record[one] = data[one] 
    result = record.save()
    return result.id, 201

@records.route("/records/<int:id>", methods=["GET"])
def get_one(id):
    record = Record.query.get_or_404(id)
    return record, 200

@records.route("/records/<int:id>", methods=["DELETE"])
def delete_one(id):
    record = Record.query.get_or_404(id)
    record.delete()
    return id, 204

