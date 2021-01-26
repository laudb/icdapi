from . import records

from app.models import Record


@records.route("/status", methods=["GET"])
def status():
    return f"diagnose app: Version 1"

@records.route("/records", methods=["POST"])
def create():
    payload = request.get_json()
    result = Record.save(payload)
    return str(result)