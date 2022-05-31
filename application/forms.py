
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, SelectField, widgets

app = Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'


class RegisterForm(FlaskForm):
    first_name = StringField('First Name: ')
    last_name = StringField('Last Name: ')
    d_o_b = DateField('Date of Birth: ')
    email = StringField('Email Address: ')
    address_1 = StringField('Address line 1: ')
    address_2 = StringField('Address line 2: ')
    post_code = StringField('Postcode: ')
    updates = 
    submit = SubmitField('Register')
    

