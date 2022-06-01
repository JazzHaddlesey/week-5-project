
from application import app, db
from application.models import Authors, Books 
from flask import Flask, render_template, request, url_for
from flask_wtf import FlaskForm
from sqlalchemy import null
from application.forms import RegisterForm, SearchForm, AddForm, DeleteForm
import os



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods = ['GET','POST'])
def search():
    message = ""
    var1 = Books.query.filter_by(name = '').all()
    var2 = Authors.query.filter_by(name = '').all()
    form = SearchForm()
    
    if request.method == 'POST':
        searched = form.searched.data
        
        if len(searched) == 0:
            message = 'Please enter name of author, or book'
            
        else:
            message = 'Results: \n'
            
    return render_template('search.html', form = form, message = message)

@app.route('/add')
def add():
    new_book = Books(name = input("New Book"))
    db.session.add(new_book)
    db.session.commit()
    return "Added new game to database"
   

@app.route('/delete/<intid>')
def delete():
    btd = Books.query.get(id)
    db.session.delete(btd)
    db.session.commit
    return f'{btd.name}, has been deleted'

@app.route('/update/<name>')
def update(name):
    first_book = Books.query.first()
    first_book.name = name
    db.session.commit()
    return f'{first_book.name}, has been updated'

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register', methods = ['GET','POST'])
def register():
    message = ""
    form = RegisterForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        d_o_b = form.d_o_b.data
        email = form.email.data
        post_code = form.post_code.data
        

        if len(first_name) == 0 or len(last_name) == 0 or d_o_b == null or len(email) == 0 or len(post_code) == 0:
            message = "Please supply all information"
            
        else:
            message = f'Thank you {first_name} {last_name}, you have successfully registered.'
            
    return render_template('register.html', form=form, message=message)


    