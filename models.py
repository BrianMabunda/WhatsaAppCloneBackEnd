# from main import *
# from main import app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

    def __repr__(self):
        return f"{self.id}:{self.name}"


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    key = db.Column(db.Integer)

    def __repr__(self):
        return f"{self.id}:{self.name}:{self.key}"
