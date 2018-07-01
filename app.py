import os
import json
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import mysql.connector as db
from config import *
    
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

class User(db.Model):
   __tablename__ = 'users'
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(80), unique=True)
   email = db.Column(db.String(120), unique=True)

   def __init__(self, username, email):
       self.username = username
       self.email = email

   def __repr__(self):
       return '' % self.username


@app.route("/users")
def users_index():
   to_json = lambda user: {"id": user.id, "name": user.username, "email": user.email}
   return json.dumps([to_json(user) for user in User.query.all()])

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)