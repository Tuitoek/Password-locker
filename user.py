class User:

    '''
    Class for generating instances for user.
    '''


    pass
    user_list=[];
    account_list=[];


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

    def register_user(self):
        """
        register_user method registers users details into user_list 
        """
        User.user_list.append(self)    
       

class Credential:

    """
    Class that generates instances for credentials.
    """
    pass
    credential_list = [];
    user_credential_list = [];

    def __init__(self,account_name,password):

            """

            Args:
                account_name : New  credentials account name.
                password : New credentials password.

            self.account_name = account_name
            self.password = password 
                

            """ 

    def __init__(self,account_name,user_name,password):  

        """

        Args:
            account_name: New user credentials account.
            user_name:New user credentials username.
            password:new user credentials password.

        self.user_name = user_name
        self.password = password 

        """  

    def register_user(self):
        """
        method that registers and saves objects into our user_list
        """        
        User.user_list.append(self)

    