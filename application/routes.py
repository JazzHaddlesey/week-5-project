
from application import app, db
from application.forms import AddForm, DeleteForm, UpdateForm
from application.models import Authors, Books 
from flask import Flask, render_template, request, url_for, redirect
from flask_wtf import FlaskForm
from sqlalchemy import null
import os



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods = ['GET', 'POST'])
def add():
    form = AddForm()
    message =''
    if request.method == 'POST' and form.validate():
        new_author = Authors(name = form.add_author.data)
        new_book = Books(name = form.add_book.data)
        message = 'Has been added to library'
        db.session.add(new_book)
        db.session.add(new_author)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', form = form, message = message)

@app.route('/read', methods = ['GET'])
def read():
    book = Books.query.all()
    author =Authors.query.all()
    return render_template('read.html', author=author, book=book)

@app.route('/update', methods = ['GET', 'POST'])
def update():
    form = UpdateForm()
    message = ''
    if request.method == 'POST' and form.validate():
        atu = Authors(name = form.update_author.data)
        btu = Books(name = form.update_book.data)
        db.session.update(btu)
        db.session.update(atu)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', form = form, message = message)
   
@app.route('/delete', methods = ['GET', 'POST'])
def delete():
    form = DeleteForm()
    message = ''
    if request.method == 'POST' and form.validate():
        atd = Authors(name = form.delete_author.data)
        btd = Books(name = form.delete_book.data)
        db.session.delete(btd)
        db.session.delete(atd)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('delete.html', form = form, message = message)

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


    