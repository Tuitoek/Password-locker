import unittest

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
