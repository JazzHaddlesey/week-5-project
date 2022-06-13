from application import db
from flask_sqlalchemy import SQLAlchemy
from application.models import Authors, Books


db.drop_all()
db.create_all()

test_author_1 = Authors(name = 'R.F.Kuang')
test_author_2 = Authors(name = 'J.R.R.Tolkien')
test_author_3 = Authors(name = 'J.K.Rowling')
test_book_1 = Books(name = 'The Dragon Republic')
test_book_2 = Books(name = 'The Hobbit')
test_book_3 = Books(name = "Harry Potter and The Philosopher's stone")
db.session.add(test_author_1)
db.session.add(test_author_2)
db.session.add(test_author_3)
db.session.add(test_book_1)
db.session.add(test_book_2)
db.session.add(test_book_3)
db.session.commit()

