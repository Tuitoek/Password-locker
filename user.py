import string
import random
import unittest

class User:

    '''
    Class for generating instances for user.
    '''



    user_list=[]


    def __init__(self,first_name,last_name,email,username):

            '''
                __init__ method that helps us define properties for our objects.

                Args:
                    first_name : New user first name.
                    last_name : New user last name.
                    email : New user email address.
                    username : New user username.

                self.first_name = first_name
                self.last_name = last_name
                self.email = email
                self.username = username


            '''
            self.first_name = first_name
            self.last_name = last_name
            self.email = email
            self.username = username

    def save_user(self):
        """
        method that registers and saves objects into our user_list
        """
        User.user_list.append(self)


class Credential:

    """
    Class that generates instances for credentials.
    """

    credential_list = []

    def __init__(self,account_name,password):

            """

            Args:
                account_name : New  credential account name.
                password : New credential password.

            self.account_name = account_name
            self.password = password


            """
            self.account_name = account_name
            self.password = password

    def create_credentials(self):
        """
        For creating a new credential account

        """
        Credential.credential_list.append(self)

    def  pass_gen(size = 8,chars=string.ascii_letters + string.digits + string.punctuation):
        return ''.join(random.choice(chars)for _ in range(size))


    def save_credential(self):
        """
        Allows the user to save their credentials
        """
        Credential.credential_list.append(self)

    # @classmethod
    # def find_by_account_name(cls,account_name):
    #     """
    #     method returns the credential list
    #
    #     """
    #     for credential in cls.user_list:
    #         if user.account_name == account_name:
    #             return credential

    def delete_credentials(self):
        """
        Enables the user to delete some credentials

        """
        Credential.credential_list.remove(self)

    @classmethod
    def display_credentials(cls):
        """
        returns the User's credential list

        """
        return cls.credential_list
