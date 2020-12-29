import sys
from ApplicantMenu import ApplicantMenu
import HRMenu
from CW2DBLocal import Database

loginMenuState = True
applicantMenuState = False
HRMenuState = False
DB = Database()
AM = ApplicantMenu(DB)

#Login
while loginMenuState == True:
    print('Welcome to the database!')
    print('Please select an option')
    print('1. Login to the database')
    print('2. Register a new account')
    print('3. Exit program')
    loginOptionChosen = input("Enter your option here to continue: ")
    if loginOptionChosen == "1":
        DB.verifyAccount()
        loginMenuState = False
        applicantMenuState = True
        #HRMenuState = True
    elif loginOptionChosen == "2":
        DB.createApplicantAccount()
        #DB.createHRAccount()
    elif loginOptionChosen == "3":
        DB.closeDataBase()
        loginMenuState = False
    elif loginOptionChosen == "4":
        DB.testDB()

    else:
        print("Incorrect input, please try again.")

while applicantMenuState == True:
    print('Please select an option')
    print('1. Make new job application')
    print('2. View job application results')
    print('3. Exit program')
    optionChosen = input("Enter your option here to continue: ")

    if optionChosen == "1":
        print('Create your new application! Please select your option to continue:')
        AM.createNewApplication()
    elif optionChosen == "2":
        AM.reviewSubmittedApplication()
    elif optionChosen == "3":
        print('Thank you for using the application!')
        DB.closeDataBase()
        applicantMenuState = False;
    elif optionChosen == "4":
        DB.retrieveApplicationSubmission()
    else:
        print("Incorrect input, please try again.")


while HRMenuState == True:
    print('Welcome! Please select an option')
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
    else:
        print("Incorrect input, please try again.")






