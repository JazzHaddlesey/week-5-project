from application import db
from flask_sqlalchemy import SQLAlchemy
from application.models import Authors, Books


db.drop_all()
db.create_all()

author_1 = Authors(name = 'R.F.Kuang', country = 'China')
author_2 = Authors(name = 'J.R.R.Tolkien', country = 'UK')
author_3 = Authors(name = 'J.K.Rowling', country = 'UK')
book_1 = Books(name = 'The Dragon Republic', author = 1)
book_2 = Books(name = 'The Hobbit', author = 2)
book_3 = Books(name = "Harry Potter and The Philosopher's stone", author = 3)
db.session.add(author_1)
db.session.add(author_2)
db.session.add(author_3)
db.session.add(book_1)
db.session.add(book_2)
db.session.add(book_3)
db.session.commit()

