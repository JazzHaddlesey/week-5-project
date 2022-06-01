from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =  "sqlite:///data.db" #os.getenv("DATABASE_URI")
app.config['SECRET_KEY'] = 'sceret key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from application import routes

