import unittest
from app import app
from app.models import User
import hashlib
## test models.py 

class UserTestCase(unittest.TestCase):

    def setUp(self):
        # This will be called before each test
        self.valid_email = "noormmlk@gmail.com"
        self.user        = User(username="Noor", email= self.valid_email)
    
    def test_hash(self):
        # Test for correct URL with SHA256 of the email
        expected_hash = hashlib.sha256(self.valid_email.encode()).hexdigest()
        expected_url  = f"https://gravatar.com/avatar/{expected_hash}?d=identicon&s=80"
        self.assertEqual(self.user.avatar(80), expected_url)

    def test_email_trimming(self):
        # Test that avatar works even with extra spaces around the email
        user          = User(username="Noor", email= "  noor@gmail.com   ")

        expected_hash = hashlib.sha256(user.email.strip().encode()).hexdigest()
        expected_url  = f"https://gravatar.com/avatar/{expected_hash}?d=identicon&s=80"        
        self.assertEqual(user.avatar(80), expected_url)

    def test_case_insensitivity(self):
        # Test that avatar method is case insensitive
        user          = User(username="Noor", email= "Noor@Gmail.com")
        expected_hash = hashlib.sha256(user.email.encode()).hexdigest()
        expected_url  = f"https://gravatar.com/avatar/{expected_hash}?d=identicon&s=80"        
        self.assertEqual(user.avatar(80), expected_url)
      
    
if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(UserTestCase))
    #suite.addTest(unittest.TestLoader().loadTestsFromTestCase())
    unittest.TextTestRunner().run(suite)




