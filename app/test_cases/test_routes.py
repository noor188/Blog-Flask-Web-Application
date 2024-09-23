import unittest
from app import app
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

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(UserProfileTestCase))
    #suite.addTest(unittest.TestLoader().loadTestsFromTestCase())
    unittest.TextTestRunner().run(suite)




