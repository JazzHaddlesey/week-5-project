
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, SelectField
from wtforms.validators import DataRequired
from wtforms.widgets import CheckboxInput

app = Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'


class CustomerForm(FlaskForm):
    first_name = StringField('First Name: ')
    last_name = StringField('Last Name: ')
    d_o_b = DateField('Date of Birth: ')
    email = StringField('Email Address: ')
    address = StringField('Address: ')
    post_code = StringField('Postcode: ')
    submit = SubmitField('Register')
    
class SearchForm(FlaskForm):
    a_search = StringField('Enter Author Name or Book Title: ')
    b_search = StringField('Enter Book Title: ')
    submit = SubmitField('Search')
    
class AddForm(FlaskForm):
    author_name = StringField('Authors name: ')
    book_name = StringField('Book name: ')
    submit = SubmitField('Submit')
    
class DeleteForm(FlaskForm):
    author_name = StringField('Delete; Authors name: ')
    book_name = StringField('Delete; Book name: ')
    submit = SubmitField('Submit')    

    

