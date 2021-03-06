from flask_testing import LiveServerTestCase
from selenium import webdriver
from urllib.request import urlopen
from flask import url_for
from application import app, db
from application.forms import AddForm, DeleteForm, UpdateForm
from application.models import Authors, Books

# class TestBase(LiveServerTestCase):
#     def create_app(self):
#         app.config.update(
#             SQLALCHEMY_DATABSE_URI = 'sqlite:///test.db',
#             LIVESERVER_PORT = 5050,
#             DEBUG = True,
#             TESTING = True
#         )
#         return app

#     def setUp(self):
#         chrome_options = webdriver.chrome.options.Options()
#         chrome_options.add_argument('--headless')
#         self.driver = webdriver.Chrome(options = chrome_options)
#         db.create_all()
#         self.driver.get('http://localhost:5050/add')

#     def tearDown(self):
#         self.driver.quit()
#         db.drop_all()

# class TestAddItem(TestBase):
#     def submit_input(self, input):
#         self.driver.find_element_by_xpath('/html/body/div[2]/div/form/input[1]').send_keys(input)
#         self.driver.find_element_by_xpath('/html/body/div[2]/div/form/input[2]').send_keys(input)
#         self.driver.find_element_by_xpath('/html/body/div[2]/div/form/input[3]').click()

#     def test_add_form(self):
#         test_case = 'R.F.Kuang'
#         self.submit_input(test_case)
#         assert Authors.query.get(1).name == 'R.F.Kuang'