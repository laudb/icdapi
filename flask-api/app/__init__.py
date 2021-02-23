from flask import Flask, jsonify
from flask_validator import validate_common, Validator
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Command, Shell
import os, config

db = SQLAlchemy()
migrate = Migrate()

# variables
db_user = os.getenv("db_user")
db_password = os.getenv("db_password")
db_host = os.getenv("db_host")
db_name = os.getenv("db_name")
db_port = os.getenv("db_port")
test_db_name = os.getenv("test_db_name")

# error
def resource_not_found(e):
    return jsonify(error=str(e)), 404

def create_app(input):
    app = Flask(__name__)
    Validator(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_object(input)
    db.init_app(app)
    migrate.init_app(app, db)

    from .core import records as r
    app.register_blueprint(r, url_prefix='/api/v1')
    app.register_error_handler(404, resource_not_found)

    return app