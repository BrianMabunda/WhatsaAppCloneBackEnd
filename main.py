from ast import Try
from enum import unique
from fileinput import filename
import mimetypes
from typing import KeysView
from urllib import response
from black import out
from flask import Flask, Response, jsonify, request
from flask_cors import CORS
from pyparsing import replaceWith
from sqlalchemy import JSON, Index
from models import *
from db import *
from werkzeug.utils import secure_filename
from markupsafe import escape


app = Flask(__name__)
CORS(app, resources={r"*": {"origin": "*"}})
# api_conf = {"origins": ["http://localhost:5000"], "method": ["GET"]}
cors = CORS(app, resources={r"*": {"origin": "*"}})
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data1.db"
db_init(app)


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


@app.route("/uploadPic", methods=["POST"])
def upload():
    print("---------------------")

    try:
        print(len(request.form["image"]))
        print(type(request.form["image"]))
        print("file")
    except:
        pass
    print("---------------------")
    #
    # if not pic:
    #     return "NO PIC", 404
    #
    pic = request.form["image"]
    mimetype = "image/png"
    filename = "photo.png"
    key = request.form["key"]
    print(key)
    img = Image(img=pic, mimetype=mimetype, name=filename, key=key)
    db.session.add(img)
    db.session.commit()
    return "Uploaded"


def extract(line, id):
    output = []
    for x in line.split(","):
        if id == 1:
            x = int(x)
        else:
            pass
        output.append(x)
    return output


@app.route("/getPic", methods=["POST"])
def getPic():
    # print(request.form)
    names = request.form["names"]
    keys = request.form["keys"]
    names = names[1 : len(names) - 1]
    keys = keys[1 : len(keys) - 1]
    keys = extract(keys, 1)
    names = extract(names, 0)
    try:
        for index in range(0, len(names)):
            print("Name" + names[index] + " Key: " + keys[index])

    except:
        pass
    print("---------------------")
    print("Hr")
    output = []
    Data = Image.query.all()
    for index in range(0, len(names)):
        temp_output = []
        for data in Data:
            image = {"img": data.img, "name": data.name, "mimetype": data.mimetype}
            if data.key == int(keys[index]):
                temp_output.append(data.img)
                print(data.key)
        if len(temp_output) > 0:
            # print(temp_output)
            output.append({names[index]: temp_output})
            temp_output.clear()
            print("hello")
    # print(output)
    return {"Image": output}


@app.route("/get/<names>/<keys>", methods=["GET"])
def get(names, keys):
    keys = extract(keys, 1)
    names = extract(names, 0)
    print(names)
    print(keys)
    output = []
    Data = Image.query.all()
    for i in range(len(keys)):
        for data in Data:
            if data.key == keys[i]:
                print("True")
                print(data.key, keys[i])
                output.append(
                    {"id": data.id, "name": names[i], "key": keys[i], "image": data.img}
                )
            else:
                pass
    return {"Image": output}
