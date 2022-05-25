from sqlalchemy import asc
from application import app, db
from flask import Flask, render_template
from flask_navigation import Navigation
  
app = Flask(__name__)
nav = Navigation(app)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/search')
def search_page():
    return render_template('search.html')
