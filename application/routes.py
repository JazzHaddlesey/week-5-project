
from application import app, db
from application.models import Authors
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from sqlalchemy import null
from wtforms import StringField, SubmitField, DateField, IntegerField, SelectField
import forms

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register', methods = ['GET','POST'])
def register():
    message = ""
    form = forms.RegisterForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        d_o_b = form.d_o_b.data
        

        if len(first_name) == 0 or len(last_name) == 0 or d_o_b == null:
            message = "Please supply all information"
            
        else:
            message = f'Thank you, {first_name} {last_name}'
            
    return render_template('register.html', form=form, message=message)


    