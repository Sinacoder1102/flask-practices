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