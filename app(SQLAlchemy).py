from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

file_dir = os.path.dirname(__file__)
goal_route = os.path.join(file_dir,"datbase.db")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + goal_route

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(60))

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return goal_route
    
-----------------------------------------------------------------------------------
# Adding users
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

file_dir = os.path.dirname(__file__)
goal_route = os.path.join(file_dir,"database.db")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + goal_route

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(60))

    def __repr__(self):
        return self.email

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    users = User.query.all()
    return render_template('index.html' , users=users)

@app.route('/add')
def adduser():
    try:
        user = User(email = 'Sina')
        db.session.add(user)
        db.session.commit()
        return "User added Successfully"
    except Exception as ex:
        return f"The error is {ex}"
-------------------------------------------------------------------------------------------
# Editing
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

file_dir = os.path.dirname(__file__)
goal_route = os.path.join(file_dir,"database.db")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + goal_route

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(60))

    def __repr__(self):
        return self.name

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    goal_str = "sin"
    users = User.query.filter(User.name.like(f"{goal_str}%")).all()
    return render_template('index.html',users=users)

@app.route('/add')
def adduser():
    try:
        user = User(name = "Sina")
        db.session.add(user)
        db.session.commit()
        return "User added Successfully"
    except Exception as ex:
        return f"ERROR : {ex}"

@app.route('/update')
def updateuser():
    try:
        goal_user = User.query.filter_by(name = 'Sina').first()
        goal_user.name = "Sina1102"
        return 'User updated successfully! , <a href"/">Home</a>'
    except Exception as ex:
        return f"Error is {ex}"
--------------------------------------------------------------------------------------
# making relationship between tables
from flask import Flask,render_template
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

file_dir = os.path.dirname(__file__)
goal_route = os.path.join(file_dir , "database.db")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + goal_route

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(60) , nullable = False)

    def __repr__(self):
        return self.name

class Writer(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(60) , nullable = False)

class Car(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(60) , nullable = False)
    writer_id = db.Column(db.Integer() , db.ForeignKey("writer.id"))
    writer = db.Relationship("Writer" , backref = db.backref("cars"))

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return "Hello world"

@app.route("/addbooks")
def bookadding():
    try:
        writer = Writer(name = "Sina")
        car = Car(name = "The car" , writer = writer)
        writer.cars.append(car)
        db.session.add(car)
        db.session.commit()
        return "Successfully added(car) <a href='/books'>See books</a>"
    except Exception as ex:
        return f"Failed {ex}"

@app.route("/books")
def show():
    car = Car.query.all()
    return render_template("index.html" , car = car)
