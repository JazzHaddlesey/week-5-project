
from application import db, app


class Authors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    
class Books(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30))
    author = db.Column(db.Integer, db.ForeignKey('authors.id'))
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    d_o_b = db.Column(db.Date)
    email = db.Column(db.String(50), unique = True)
    address_1 = db.Column(db.String(30))
    address_2 = db.Column(db.String(30))
    post_code = db.Column(db.String(10))
    
    
class Orders(db.Model):
    id = db.Column(db.Interger, primary_key = True)
    books = db.Relationship('books', backref = 'books_idbr')
    user_id = db.Column(db.Interger, db.ForeignKey('user.id'))
        
    
    
class Book_Order(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    



    

  
    
    
