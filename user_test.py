import unittest
import string
import random

from user import Credentials
from user import User

class TestUser(unittest.TestCase):
    '''
    Test Class that defines test cases for the user

    Args:
        unittest.TestCase : TestCase class that helps in creating test cases

    '''

    def setUp(self):
        '''
        set up method to run before each test cases.
        '''
        self.new_user = User("Sarah","Tuitoek","sjtoek13@gmail.com","tui")

    def test_intit(self):
        '''
        test_init tests if the object is initialized properly
        '''    

        self.assertEqual(self.new_user.first_name,"Sarah")
        self.assertEqual(self.new_user.last_name,"Tuitoek")
        self.assertEqual(self.new_user.email,"sjtoek13@gmail.com")
        self.assertEqual(self.new_user.username,"Tui")

    def test_register_user(self):
        """
        test_register_user case to test if the user has been registred
        """
        self.new_user.test_register_user(self)
        self.assertEqual(len(User.user_list),1)

    def test_login_user(self):
        """
        test_login_user case to test if the user can log in into the account.
        """
        self.new_user.test_login_user()
        test_user = User("Test","test@user.com","username")
        
        user_exists = User.user_list(username)

        self.assertTrue(user_exists)

    def create_account(self):
        """
        test allows users to create new account and generate passwords.
        """
        self.new_account.create_account()
        self.assertEqual(len(User.user_credentials_list),1)

    def create_credentials(self):
        """
        Function to save a newly created user intsnace
        """ 
        Credential.credential_list.append(self)

    def  pass_gen(size = 8,chars=string.ascii_letters + string.digits + string.punctuation):
        return ''.join(random.choice(chars)for _ in range(size))

    def save_credentials(self):
        """
        Function to save a newly created credential
        """
        self.new_credential.save_credentials()
        self.assertEqual(len(Credential.credential_list))

         



        