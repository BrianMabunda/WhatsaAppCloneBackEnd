# from main import *
from db import db


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


class Chats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chat_time = db.Column(db.String(80), unique=False)
    key = db.Column(db.Integer)
    text = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.id}:{self.chat_time}:{self.text}:{self.key}"


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.Integer)
    img = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
