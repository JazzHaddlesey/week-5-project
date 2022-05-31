from pickle import FALSE
from application import db

class Authors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    author = db.column(db.Integer, db.ForeignKey('authors.id'))
    
