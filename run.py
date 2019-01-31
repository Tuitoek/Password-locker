#!/usr/bin/env python3.7
from user import User
from user import Credential

def create_user(first_name,last_name,username,email,password):
    """
    Function that allows one to create a user account
    """
    new_user = User(first_name,last_name,username,email,password)
    return new_user

def save_user(user):
    """
    Function for a user to log in
    """
    User.save_user(self)

def save_credential(credential):
    """
    Function that saves credentials
    """
    credential.save_credential()

def delete_credentials(credential):
    """
    Function that deletes credentials
    """
    credential.delete_credentials()

def display_credentials(credential):
    """
    Function that displays all credentials.
    """
    return Credential.display_credentials()

def main():
    print("Hello Welcome to your user list. What is your name?")
    username = input()

    print(f"Hello {username}. what would you like to do?")
    print('\n')

    while True:

        print("Use these short codes : 1 - Log in to save user, 2 - create credentials, 3 - display credentials, 4 - delete credentials, 5 -find credentials, ex -exit  ")

        short_code = input().lower()

        if short_code == '1':
            print("Please register")

            print ("First name ....")
            first_name = input()

            print("Last name ...")
            last_name = input()

            print("Email address ...")
            email = input()

            print("Username ...")
            username = input()

            print("Enter your password")
            password = input()

            save_user(create_user(first_name, last_name, username, email, password))
            print ('\n')

            print(f"New User {first_name} created")
            print ('\n')

        elif short_code == '2':
            print("Enter account-name")
            account_name = input(" ")

            print("Enter password")
            password = input(" ")

            save_credential(create_credentials(
              account_name, password))
            print("\n")
            print(
            f"New credentials {ac-name},{new-ps} created")

        elif short_code == '3':

            if display_credentials():
                print("Here is a list of all your credentials")
                print('\n')

                for credential in display_c():
                        print(f"{credential.account_name} {credential.password}")

                print('\n')
            else:
                    print('\n')
                    print("You dont seem to have any credentials saved yet")
                    print('\n')

        elif short_code == '4':

            print("Do you want to delete this credential,Y/n?")
            answer = input()

            if(answer == 'Y'):
                print("Are you sure that you want to delete this credential,Y,n")
                pick = input()

                if (pick == 'Y'):
                    {{credential.remove()}}
                    print("Credential was successfully removed")

                else:
                    print("Credential not removed")

            else:
                print("Credential will not be deleted")

        elif short_code == "ex":
            print("Bye .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
    main()
