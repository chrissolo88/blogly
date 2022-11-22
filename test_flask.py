from unittest import TestCase
from app import app
from models import db,User 

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_shop_test'
app.config['SQLALCHEMY_ECHO'] = False
app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

class BloglyViewsTestCase(TestCase):
    def setUp(self):
        User.query.delete()
        user = User(first_name='Test',last_name='User',img_url='test.jpg')
        db.session.add(user)
        db.session.commit()
        self.user_id = user.id
        
    def tearDown(self):
        db.session.rollback()
        
    def test_list_user(self):
        with app.test_client() as client:
            resp = client.get('/users')
            html = resp.get_data(as_text=True)
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn('Test User',html)
            
    def test_home(self):
        with app.test_client() as client:
            resp = client.get(f'/')
            html = resp.get_data(as_text=True)
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h2>Recent Posts:</h2>',html)
            
    def test_add_user(self):
        with app.test_client() as client:
            d = {"first_name":"Test2","last_name":"User2","img_url":"test.jpg"}
            resp = client.post("/users/new", data=d,follow_redirects=True)
            html = resp.get_data(as_text=True)
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn("Test2 User2", html)