from flask import Flask,jsonify
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Command, Shell
import os, config

db = SQLAlchemy()
migrate = Migrate()

def resource_not_found(e):
    return jsonify(error=str(e)), 404

def create_app(input):
    app = Flask(__name__)

    app.config.from_object(input)

    db.init_app(app)
    migrate.init_app(app, db)

    from .core import records as r
    app.register_blueprint(r, url_prefix='/api/v1')
    app.register_error_handler(404, resource_not_found)

    return app