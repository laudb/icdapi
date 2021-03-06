import os
from app import db, create_app
from app.models import Record
from flask_script import Manager, Shell
from flask_migrate import MigrateCommand

app = create_app(os.getenv("APP_ENV"))
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, Record=Record)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()