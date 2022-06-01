from application import db
from flask_sqlalchemy import SQLAlchemy
from application.models import Authors, Books, Customer


db.drop_all()
db.create_all()

test_author_1 = Authors(name = 'R.F.Kuang')
test_author_2 = Authors(name = 'J.R.R.Tolkien') 
test_book_1 = Books(name = 'The Dragon Republic')
test_book_2 = Books(name = 'The Hobbit')
test_cust_1 = Customer(first_name = 'John')
db.session.add(test_author_1)
db.session.add(test_author_2)
db.session.add(test_book_1)
db.session.add(test_book_2)
db.session.add(test_cust_1)
db.session.commit()

