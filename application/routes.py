
from application import app, db
from application.models import Authors, Books 
from application.forms import Add
from flask import Flask, render_template, request, url_for
from flask_wtf import FlaskForm
from sqlalchemy import null
import os



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods = ['GET', 'POST'])
def add():
    form = Add()
    if request.method == 'POST' and form.validate():
        new_book = Books(form.data.add)
        db.session.add(new_book)
        db.session.commit()
        return redirect(urlf_for('index'))
    return render_template('add.html', form = form)

@app.route('/read')
def read():
    all_books = Books.query.all()
    books_string = ""
    for book in all_books:
        books_string += "<br>"+ book.name
    return books_string

@app.route('/update/<name>')
def update(name):
    first_book = Books.query.first()
    first_book.name = name
    db.session.commit()
    return f'{first_book.name}, has been updated'
   
@app.route('/delete')
def delete():
    btd = Books.query.first()
    db.session.delete(btd)
    db.session.commit()
    return f'{btd.name}, has been deleted'

# @app.route('/register', methods = ['GET','POST'])
# def register():
#     message = ''
#     form = CustomerForm()

#     if request.method == 'POST':
#         if form.validate_on_submit():
#             cust = Customer(first_name = form.first_name.data, last_name = form.last_name.data, 
#                                  d_o_b = form.d_o_b.data, email = form.email.data, address = form.address.data, 
#                                  post_code = form.post_code.data)
#             db.session.add(cust)
#             db.session.commit()
#             return f' Thank you {cust.first_name} {cust.last_name} you have successfully registered.'
            
#     return render_template('register.html', form = form, meassage = message)


    