
from application import app, db
from application.models import Authors, Books 
from flask import Flask, render_template, request, url_for
from flask_wtf import FlaskForm
from sqlalchemy import null
from application.forms import CustomerForm, SearchForm, AddForm, DeleteForm
from application.models import Customer
import os



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods = ['GET','POST'])
def search():
    all_books = Books.query.all()
    all_authors = Authors.query.all()
    all_cust = Customer.query.all()
    form = SearchForm()
    
    if request.method == 'POST':
        if all_books in form:
            return Books.name
            
    return render_template('search.html', form = form, )

@app.route('/add/<name>')
def add():
    new_book = Books.name
    db.session.add(new_book)
    db.session.commit()
    return f"Added {new_book} to database"
   

@app.route('/delete/<name>')
def delete():
    btd = Books.query.get(Books.name)
    db.session.delete(btd)
    db.session.commit
    return f'{btd.name}, has been deleted'

@app.route('/update/<name>')
def update(name):
    first_book = Books.query.first()
    first_book.name = name
    db.session.commit()
    return f'{first_book.name}, has been updated'

@app.route('/read')
def read():
    all_books = Books.query.all()
    all_authors = Authors.query.all()
    all_cust = Customer.query.all()
    return render_template('read.html', all_books = all_books, all_authors = all_authors, all_cust = all_cust)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register', methods = ['GET','POST'])
def register():
    message = ''
    form = CustomerForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            cust = Customer(first_name = form.first_name.data, last_name = form.last_name.data, 
                                 d_o_b = form.d_o_b.data, email = form.email.data, address = form.address.data, 
                                 post_code = form.post_code.data)
            db.session.add(cust)
            db.session.commit()
            message = f' Thank you {cust.first_name} {cust.last_name} you have successfully registered.'
            
    return render_template('register.html', form = form, meassage = message)


    