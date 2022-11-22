from unittest import TestCase
from app import app
from models import db,User

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_shop_test'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()

class UserModelTestCase(TestCase):
    def setUp(self):
        User.query.delete()
        
    def tearDown(self):
        db.session.rollback()
        
    def test_fullname(self):
        user = User(first_name='test',last_name='user',img_url='test.jpg')
        self.assertEquals(user.fullname, "Test User")
