import sys
import ApplicantMenu
import HRMenu
from CW2DBLocal import Database

loginMenuState = True
registarState = False
loginState = False
authenticateUser = False
applicantMenuState = False
HRMenuState = False
global usernameCheck
DB = Database()

#Login
while loginMenuState == True:
    print('Welcome to the database!')
    print('Please select an option to continue:')
    print('1. Login to the database')
    print('2. Register a new account')
    print('3. Exit program')
    loginOptionChosen = input("Enter your option here to continue: ")
    if loginOptionChosen == "1":
        loginState = True
        loginMenuState = False
    elif loginOptionChosen == "2":
        registarState = True
        loginMenuState = False
    elif loginOptionChosen == "3":
        DB.closeDataBase()
        loginMenuState = False

while registarState == True:
    DB.createTable()
    DB.createUserName()
    



while loginState == True:
    usernameCheck = input('Please enter in your username: ')
    passwordCheck = input('Please enter in your password: ')
    

#Login Success
    if authenticateUser == True:
        loginState = False
        applicantMenuState = True

while applicantMenuState == True:
    print('1. Make new job application')
    print('2. View job application results')
    print('3. Exit program')
    optionChosen = input("Enter your option here to continue: ")

    if optionChosen == "1":
        ApplicantMenu.ApplicantMenu.createNewApplication(usernameCheck)
    elif optionChosen == "2":
        ApplicantMenu.ApplicantMenu.reviewSubmittedApplication()
    elif optionChosen == "3":
        print('Thank you for using the application!')
        DB.closeDataBase()
        applicantMenuState = False;

while HRMenuState == True:
    print('Welcome! Please select an option to continue:')
    print('1. Search new job application')
    print('2. View job application results')
    print('3. Exit program')
    optionChosen = input("Select option here: ")

    if optionChosen == "1":
        print('Search!')
    elif optionChosen == "2":
        print('Edit!')
    elif optionChosen == "3":
        print('Thank you for using the application!')
        DB.closeDataBase()
        HRMenuState = False;






