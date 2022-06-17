from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from application import app, db
from flask_testing import TestCase
from application.models import Authors, Books

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = "sqlite:///test.db",
            SQLALCHEMY_TRACKING_MODIFICATIONS = False,
            SECERT_KEY = "secret key",
            WTF_CSRF_ENABLED = False
        )
        return app
    
    def setUp(self):
        author1 = Authors(name="R.F.Kuang")
        book1 = Books(name="The Dragon Republic")
        db.create_all()
        db.session.add(author1)
        db.session.add(book1)
        db.session.commit()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
class TestViewHome(TestBase):
    def test_get_home(self):
        response = self.client.get(url_for("index"))
        self.assert200(response)

class TestViewAdd(TestBase):
    def test_get_add(self):
        response = self.client.get(url_for("add"))
        self.assert500(response)

class TestAddBook(TestBase):
    def test_post_add(self):
        response = self.client.post(url_for('add'),
        data = dict(add = 'Book has been added'),
        follow_redirects = True
        )
        self.assert200(response)
        
class TestViewRead(TestBase):
    def test_get_add(self):
        response = self.client.get(url_for("read"))
        self.assert200(response)      
        
class TestViewUpdate(TestBase):
    def test_get_update(self):
        response = self.client.get(url_for("update"))
        self.assert500(response)

class TestUpdateBook(TestBase):
    def test_post_update(self):
        response = self.client.post(url_for('update'),
        data = dict(add = 'Book has been updated'),
        follow_redirects = True
        )
        self.assert500(response)

class TestViewDelete(TestBase):
    def test_get_Delete(self):
        response = self.client.get(url_for("delete"))
        self.assert500(response)

class TestDeleteBook(TestBase):
    def test_post_delete(self):
        response = self.client.post(url_for('delete'),
        data = dict(add = 'Book has been deleted'),
        follow_redirects = True
        )
        self.assert500(response)

