import unittest
import string
import random


from user import Credential
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
           self.new_user = User("Sarah","Tuitoek","sjtoek13@gmail.com","tui","mkambez")

        def test_intit(self):
            """
            test_init tests if the object is initialized properly
            """
            '''
            Test Class that defines test cases for the user

            Args:
                unittest.TestCase : TestCase class that helps in creating test cases

            '''

            self.assertEqual(self.new_user.first_name,"Sarah")
            self.assertEqual(self.new_user.last_name,"Tuitoek")
            self.assertEqual(self.new_user.email,"sjtoek13@gmail.com")
            self.assertEqual(self.new_user.username,"tui")
            self.assertEqual(self.new_user.password,"mkambez")

        def test_create_user(self):
            """
            Test that allows one to create a user
            """
            self.new_user.create_user()
            self.assertEqual(len(User.user_list),1)

        def test_save_user(self):
            """
            test_register_user case to test if the user has been registred
            """
            self.new_user.save_user()
            self.assertEqual(len(User.user_list),2)




class TestCredential(unittest.TestCase):
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
            self.assertEqual(self.new_credential.password,"mkambezz3")

        def test_create_credentials(self):
            """
            Function to save a newly created user intsnace
            """
            Credential.credential_list.append(self)

        def  pass_gen(size = 8,chars=string.ascii_letters + string.digits + string.punctuation):
            return ''.join(random.choice(chars)for _ in range(size))

        def test_save_credential(self):
            """
            Test function to save a newly created credential
            """
            self.new_credential.save_credential()
            self.assertEqual(len(Credential.credential_list),2)

        # def test_find_credential_by_account_name(self):
        #     """
        #     Test function for finding credentials.
        #     """
        #     self.new_credential.save_credential()
        #     test_credential=Credential("Instagram","mkambezz3")
        #     test_credential.save_credential()
        #
        #     found_credential = Credential.find_by_account_name('Instagram','mkambezz3')
        #     self.assertEqual(found_credential.ppassword,test_credential.password)

        def delete_credential(self):
            """
            Function that deletes a saved credential

            """
            self.new_credential.delete_credential()
            test_credential = Credential("account_name","sara334")
            self.assertEqual(len(Credential.credential_list),1)

        def test_display_all_credentials(self):
            """
            returns all list of all contacts

            """
            self.assertEqual(Credential.display_credentials(),Credential.credential_list)


if __name__ == '__main__':
    unittest.main()
