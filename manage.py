#!/usr/bin/env python
from flask.ext.script import Manager, Shell, Server
from example import app
from example.models import User

manager = Manager(app)
manager.add_command("runserver", Server())
manager.add_command("shell", Shell())

@manager.command
def createdb():
    from example.models import db
    db.create_all()

manager.run()
