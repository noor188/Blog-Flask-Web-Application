import unittest
from app import app, db
from app.models import User
from flask_login import login_user
## test route.py view functions

class UserProfileTestCase(unittest.TestCase):

    def setUp(self):
        '''set up a Flask test client to send
        requests to app '''
        # create a test client
        self.app = app.test_client()
        # Propagate exceptions to the test client
        self.app.testing = True
    
    def test_user_profile_get(self):
        # send a GET request to the user profile endpoint
        response = self.app.get('/profile')
        # check that the request succeeded
        self.assertEqual(response.status_code, 200)
        # check that the response contains expected content
        self.assertIn(b'User Profile', response.data)

    def test_user_profile_post(self):
        # Send POST request with example form data
        response = self.app.post('/profile', data={
            'username': 'testuser',
            'email'   : 'testuser@example.com'
        })
        # check that the request succeeded
        self.assertEqual(response.status_code, 200)
        # check that the response contains expected content
        self.assertIs(b'Profile updated', response.data)

class IndexTestCase(unittest.TestCase):

    def setUp(self):
        '''set up a Flask test client to send
        requests to app and initialize the application'''
        # create a test client
        self.client = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
    
    def login(self, username, password):
        # log the user in by posting to the login route
        return self.client.post('/login', data=dict(username= username, password= password), follow_redirects=True)
       
    def test_index_get(self):
        """ # send a GET request to the index endpoint
        #response = self.login(username='testuser', password='testpassword')
        # check that the request succeeded
        self.assertEqual(response.status_code, 200)
        # check that the response contains expected content
        self.assertIn(b'Login', response.data) """

        with self.client:
            response = self.client.get('/index')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Home', response.data)

    """ def test_index_post(self):
        # Send POST request with example form data
        pass """

    

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    #suite.addTest(unittest.TestLoader().loadTestsFromTestCase(UserProfileTestCase))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(IndexTestCase))
    unittest.TextTestRunner().run(suite)




