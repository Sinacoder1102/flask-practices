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
