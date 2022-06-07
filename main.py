from ast import Try
from enum import unique
from urllib import response
from black import out
from flask import Flask, Response, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
# api_conf = {"origins": ["http://localhost:5000"], "method": ["GET"]}
cors = CORS(app, resources={r"*": {"origin": "*"}})
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data1.db"

db = SQLAlchemy(app)


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


@app.route("/")
def index():
    output = []
    Data = Contact.query.all()
    for data in Data:
        contact = {"contacts": data.id, "Name": data.name, "Key": data.key}
        output.append(contact)
    return {"Contacts": output}


@app.route("/text")
def text():
    output = []
    Data = User.query.all()
    for data in Data:
        user = {"Name": data.name, "id": data.id}
        output.append(user)
    return {"users": output}


@app.route("/chats")
def chats():
    output = []
    Data = Chats.query.all()
    for data in Data:
        chat = {"Time": data.chat_time, "text": data.text, "key": data.key}
        output.append(chat)
    return {"Chats": output}


@app.route("/contacts")
def contacts():
    output = []
    Data = Contact.query.all()
    for data in Data:
        contact = {"id": data.id, "name": data.name, "key": data.key}
        output.append(contact)
    return {"Contacts": output}


@app.route("/sendText", methods=["POST"])
def sendText():
    # For inserting the post insidethe database
    try:
        chat = Chats(
            chat_time=request.json["time"],
            text=request.json["text"],
            key=0,
        )
        db.session.add(chat)
        db.session.commit()
        print("Chat Sucsessfully loaded in the database")

    except print(db.session.commit()):
        pass
    return "Done"
