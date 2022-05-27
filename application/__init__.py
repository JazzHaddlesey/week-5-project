from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =  "sqlite:///data.db" #os.getenv("DATABASE_URI")

db = SQLAlchemy(app)

from application import routes

