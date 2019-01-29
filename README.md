## Name of application

Password-locker

## Description

This a python developed app made for storing the user's credentials that is the history of the user's account's name and their password.It also allows one to log in as a user.

## Set-up instructions

- Fork the repository to your github account
- Clone the project on your terminal
-  Build python by usig the code below

    - if you are on Mac OS or UNIX use:
    ./configure --with-pyedeug && make -j

    - if you are on windows use
       PCbuild\build.bat -e -d

- Run the tests ./python -m test -j3

  If you are on Mac OS replace ./python with ./python.exe and if on windows use python.bat

- Create a new branch where your work for the issue will go
- Push the branch on your github page

## Dependencies

One requires .It can be installed using
- python -m pip install --target pythonFiles --implementation py --no-deps -r requirements.txt

## Technology used

Python

## Contact

If need be you can contact me at sjtoek@gmail.com

## BDD

- One can be able to log into the application
- One can save their own credentials
- One can delete credentials 
