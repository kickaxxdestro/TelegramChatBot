import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('application.db', isolation_level=None)
        self.c = self.conn.cursor()
        self.conn.commit()
        self.usernameLogged = ""

    def submitNewApplication(self, dictList):

        self.c.execute("""CREATE TABLE IF NOT EXISTS JobApply (
        ApplicationID INTEGER PRIMARY KEY AUTOINCREMENT,
        ApplicantID TEXT NOT NULL, 
        PositionedApplied TEXT NOT NULL, 
        DateApplied TEXT NOT NULL, 
        ExpectedSalary TEXT NOT NULL, 
        Availability TEXT NOT NULL,
        ConfirmJob TEXT NOT NULL)""")

        self.c.execute("""CREATE TABLE IF NOT EXISTS PersonalDetails (
        ApplicationID INTEGER PRIMARY KEY AUTOINCREMENT,
        ApplicantID TEXT NOT NULL,
        Name TEXT NOT NULL, 
        NRIC_Passport TEXT NOT NULL, 
        Address TEXT NOT NULL, 
        Postcode TEXT NOT NULL, 
        Email TEXT NOT NULL, 
        PhoneNo TEXT NOT NULL, 
        MobileNo TEXT NOT NULL, 
        DateOfBirth TEXT NOT NULL, 
        Gender TEXT NOT NULL)""")

        self.c.execute("""CREATE TABLE IF NOT EXISTS Qualifications (
        ApplicationID INTEGER PRIMARY KEY AUTOINCREMENT,
        ApplicantID TEXT NOT NULL,
        Qualification TEXT NOT NULL,
        Institution_University TEXT NOT NULL,
        Major TEXT NOT NULL,
        Grade TEXT NOT NULL,
        Year Graduated TEXT NOT NULL)""")

        self.c.execute("""CREATE TABLE IF NOT EXISTS WorkingExperiences (
        ApplicationID INTEGER PRIMARY KEY AUTOINCREMENT,
        ApplicantID TEXT NOT NULL,
        Company TEXT NOT NULL, 
        Industry TEXT NOT NULL, 
        Position TEXT NOT NULL, 
        FromMonth TEXT NOT NULL,
        FromYear TEXT NOT NULL, 
        ToMonth TEXT NOT NULL,
        ToYear TEXT NOT NULL,
        Level TEXT NOT NULL,
        Monthly Salary TEXT NOT NULL)""")

        self.c.execute("""CREATE TABLE IF NOT EXISTS ReferencesTable (
        ApplicationID INTEGER PRIMARY KEY AUTOINCREMENT,
        ApplicantID TEXT NOT NULL,
        Name TEXT NOT NULL, 
        Occupation TEXT NOT NULL, 
        Company_Organization TEXT NOT NULL, 
        ContactNo TEXT NOT NULL, 
        Email TEXT NOT NULL, 
        Relationship INTEGER NOT NULL)""")

        self.c.execute("""CREATE TABLE IF NOT EXISTS HR (
        ApplicationID INTEGER PRIMARY KEY AUTOINCREMENT,
        ApplicantID TEXT NOT NULL,
        HR_Officer TEXT NOT NULL, 
        Outcome TEXT NOT NULL, 
        Reason TEXT NOT NULL,
        Accepted TEXT NOT NULL,
        ConfirmedDate TEXT NOT NULL)""")

        self.c.execute("INSERT INTO JobApply (ApplicantID, PositionedApplied, DateApplied, ExpectedSalary, Availability, ConfirmJob) VALUES (?, ?, ?, ?, ?, ?)", (self.usernameLogged,  dictList[0]['PositionApplied'],  dictList[0]['DateApplied'],  dictList[0]['ExpectedSalary'], dictList[0]['Availability'],  dictList[0]['ConfirmJob']))

        self.c.execute("INSERT INTO PersonalDetails (ApplicantID, Name, NRIC_Passport, PostalCode, Email, HomeNo, MobileNo, DateOfBirth, Gender) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (self.usernameLogged, dictList[1]['Name'], dictList[1]['NRIC_Passport'], dictList[1]['Address'], dictList[1]['PostalCode'], dictList[1]['Email'], dictList[1]['HomeNo'], dictList[1]['MobileNo'], dictList[1]['DateOfBirth'], dictList[1]['Gender']))

        self.c.execute("INSERT INTO Qualifications (ApplicantID, Qualification, InstitutionUniversity, Major, Grade, YearGraduated) VALUES (?, ?, ?, ?, ?, ?)", (self.usernameLogged, dictList[2]['Qualification'], dictList[2]['InstitutionUniversity'], dictList[2]['Major'], dictList[2]['Grade'], dictList[2]['YearGraduated']))

        self.c.execute("INSERT INTO WorkingExperiences (ApplicantID, Company, Industry, FromMonth, FromYear, ToMonth, ToYear, Level, MonthlySalary) VALUES (?, ?, ?, ?, ?, ?, ?)", (self.usernameLogged, dictList[3]['Company'], dictList[3]['Industry'], dictList[3]['Position'], dictList[3]['FromDate'], dictList[3]['ToDate'], dictList[3]['Level'], dictList[3]['MonthlySalary']))

        self.c.execute("INSERT INTO ReferencesTable (ApplicantID, Name, Occupation, CompanyOrganization, ContactNo, Email, Relationship) VALUES (?, ?, ?, ?, ?, ?, ?)", (self.usernameLogged, dictList[4]['Name'], dictList[4]['Occupation'], dictList[4]['CompanyOrganization'], dictList[4]['ContactNo'] ,dictList[4]['Email'],dictList[4]['Relationship']))

        self.c.execute("INSERT INTO HR (ApplicantID, HR_Officer, Outcome, Reason, ConfirmedDate) VALUES (?, ?, ?, ?, ?, ?)",(self.usernameLogged, "", "", "", "", ""))

        print("Application submitted! Have a nice day!")
        
    def createApplicantAccount(self):
        self.c.execute("CREATE TABLE IF NOT EXISTS ApplicantLogin (username TEXT PRIMARY KEY, password TEXT NOT NULL)")

        userNameSet = True
        passWordSet = False
        userNameInput = ""
        while userNameSet == True:
            userNameInput = input("Please type in your new username: ")
            self.c.execute("SELECT * FROM ApplicantLogin")
            usernames = {username[0] for username in self.c.fetchall()}
            if userNameInput in usernames:
                print("This username has been taken, please try again.")
            else:
                print("Username acceptable")
                userNameSet = False;
                passWordSet = True;

        while passWordSet == True:
            passWordInput = input("Please type in your new password: ")
            print("Username: " + userNameInput + " Password: " + passWordInput)
            print("Are you okay with your new username and password?")
            confirmation = input("1 - Yes, 2 - No: ")

            if(confirmation == "1"):
                self.c.execute("INSERT INTO ApplicantLogin VALUES (\"%s\",\"%s\")"% (userNameInput, passWordInput))
                self.conn.commit()
                passWordSet = False

            elif(confirmation == "2"):
                userNameSet = True
                passWordSet = False

    def createHRAccount(self):
        self.c.execute("CREATE TABLE IF NOT EXISTS HRLogin (username TEXT PRIMARY KEY, password TEXT NOT NULL)")

        userNameSet = True
        passWordSet = False
        userNameInput = ""
        while userNameSet == True:
            userNameInput = input("Please type in your new username: ")
            self.c.execute("SELECT * FROM HRLogin")
            usernames = {username[0] for username in self.c.fetchall()}
            if userNameInput in usernames:
                print("This username has been taken, please try again.")
            else:
                print("Username acceptable")
                userNameSet = False;
                passWordSet = True;

        while passWordSet == True:
            passWordInput = input("Please type in your new password: ")
            print("Username: " + userNameInput + " Password: " + passWordInput)
            print("Are you okay with your new username and password?")
            confirmation = input("1 - Yes, 2 - No: ")

            if(confirmation == "1"):
                self.c.execute("INSERT INTO HRLogin VALUES (\"%s\",\"%s\")"% (userNameInput, passWordInput))
                self.conn.commit()
                passWordSet = False

            elif(confirmation == "2"):
                userNameSet = True
                passWordSet = False

    def verifyAccount(self):
        usernameCheck = ""
        verifySuccess = False
        while verifySuccess == False:
            usernameCheck = input('Please enter your username: ')
            self.c.execute("SELECT password FROM ApplicantLogin WHERE username = \"%s\""% (usernameCheck))
            password = {password[0] for password in self.c.fetchall()}
            if len(password) <= 0:
                print("The username does not exist, please try again.")
            else:
                passwordCheck = input('Please enter your password: ')
                if passwordCheck in password:
                    verifySuccess = True
                else:
                    print("Incorrect password, please try again.")
        else:
            print("Login success, welcome " + usernameCheck + ".")
            self.usernameLogged = usernameCheck

    def retrieveApplicationSubmission(self):
        self.c.execute("SELECT * FROM JobApply WHERE ApplicantID = \"%s\""%(self.usernameLogged))
        applicantRows = self.c.fetchall()

        self.c.execute("SELECT OUTCOME FROM HR WHERE ApplicantID = \"%s\""%(self.usernameLogged))
        outcomeRows = self.c.fetchall()
        print("1." + applicantRows[0] + "Outcome:" +outcomeRows[0])

    def retrieveAll(self):
        self.c.execute("SELECT ApplicantID FROM JobApply WHERE ApplicantID = \"%s\""%(self.usernameLogged))
        applicantRows = self.c.fetchall()

    def sortApplications():
        return None
        #Sort Database Function
        #Search Database Function

    def closeDataBase(self):
        self.c.close()
        self.conn.close()

    def testDB(self):
        self.c.execute("""CREATE TABLE IF NOT EXISTS HR (
        ApplicationID INTEGER PRIMARY KEY AUTOINCREMENT,
        ApplicantID TEXT NOT NULL,
        HR_Officer TEXT NOT NULL, 
        Outcome TEXT NOT NULL, 
        Reason TEXT NOT NULL,
        Accepted TEXT NOT NULL,
        ConfirmedDate TEXT NOT NULL)""")

        self.c.execute("INSERT INTO HR (ApplicantID, HR_Officer, Outcome, Reason, Accepted, ConfirmedDate) VALUES (?, ?, ?, ?, ?, ?)",("Tomato", "a", "a", "a", "a", "a"))
        self.c.execute("INSERT INTO HR (ApplicantID, HR_Officer, Outcome, Reason, Accepted, ConfirmedDate) VALUES (?, ?, ?, ?, ?, ?)",("Potato", "b", "b", "b", "b", "b"))

        self.c.execute("SELECT * from HR")
        applicantRows = self.c.fetchall()
        print(applicantRows)
        
   
#self.c.execute("""CREATE TABLE HRLogin (
#ID text PRIMARY KEY,
#Password text NOT NULL
#)""")

#post a new job application - 90%
#Logic and scenario - 10%
#allow job applicant to accept for job - 0% allow HR to approve application, allow applicant to accept job offer.
#reviewing the job application - 0% allow HR to edit application