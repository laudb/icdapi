from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Command, Shell
import os, config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .core import records as r
    app.register_blueprint(r)

    return app