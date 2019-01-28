import unittest
import string
import random
import pyperclip

from user import Credentials
from user import User

class TestUser(unittest.TestCase):
        """
        Test Class that defines test cases for the user

        Args:
            unittest.TestCase : TestCase class that helps in creating test cases

        """

        def setUp(self):

        """

        set up method to run before each test cases

        """
        self.new_user = User("Sarah","Tuitoek","sjtoek13@gmail.com","tui")

    def test_intit(self):
        """
        test_init tests if the object is initialized properly
        """    '''
        Test Class that defines test cases for the user

        Args:
            unittest.TestCase : TestCase class that helps in creating test cases

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




class TestCredentials(unittest.TestCase):
        """
        Test class that defines test cases for credentials

        Args:
        unittest.TestCase : TestCase class that helps in creating test cases

        """
    def setUp(self):
        """
        Set up method to run before each test cases.

        """
        self.new_credential = Credential("Instagram","mkambezz3")

    def test_init(self):
        """
        Used to check if the object is initialized properly

        """
        self.assertEqual(self.new_credential.account_name,"Instagram")
        self.assertEqual(self.new_credntial.password,"mkambezz3")

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

    def delete_credential(self):
         """
         Function that deletes a saved credential

         """
         self.new_credential.delete_credential()
         test_credential = Credential("Test","account_name","sara334")
         self.assertEqual(len(Credential.credential_list),1)

    def test_display_all_credentials(self):
        """
        returns all list of all contacts

        """
        self.assertEqual(Credential.display_credentials().credential_list)

    def test_copy_credential(self):
        """
        Test to copy the credentials account name and password

        """
        self.new_credential.save_credential()
        Credential.copy_account_name("Instagram")
        Credential.copy_password("mkambezz3")

        self.assertEqual(self.new_credential.email,pyperclip.paste())
        self.assertEqual(self.new_credential.password,pyperclip.paste())

if __name__ == '__main__':
    unittest.main()
