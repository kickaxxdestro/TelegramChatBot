import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('application.db', isolation_level=None)
        self.c = self.conn.cursor()
        self.conn.commit()

    @staticmethod
    def verifyLogin(self):
       return None

    @staticmethod
    def submitNewApplication(self, username, dictType, dict):
        self.c.execute("SELECT * FROM applicantLogin")
        
        if(str == "JobApply"):
            self.c.execute("INSERT INTO JobApply VALUES (dict[PositionApplied],dict[DateApplied],dict[ExpectedSalary],dict[Availability])")
        elif(str == "PersonalDetails"):
            self.c.execute("INSERT INTO PersonalDetails VALUES (dict['Name'],dict['NRIC_Passport'],dict['Address'],dict['PostalCode'],dict['Email'],dict['HomeNo'],dict['MobileNo'],dict['DateOfBirth'],dict['Gender'])")
        elif(str == "Qualifications"):
            self.c.execute("INSERT INTO Qualifications VALUES (dict['Qualification'],dict['InstitutionUniversity'],dict['Major'],dict['Grade'], dict['YearGraduated'])")
        elif(str == "WorkingExperiences"):
            self.c.execute("INSERT INTO WorkingExperiences VALUES (dict['Company'],dict['Industry'],dict['Position'],dict['From'],dict['To'],dict['Level'],dict['MonthlySalary'])")
        elif(str == "References"):
            self.c.execute("INSERT INTO References VALUES (dict['Name'],dict['Occupation'], dict['CompanyOrganization'], dict['ContactNo'],dict['Email'],dict['Relationship'])")

    def createTable(self):
        self.c.execute("CREATE TABLE IF NOT EXISTS applicantLogin (username TEXT, password TEXT, ID INT AUTO_INCREMENT PRIMARY KEY")


    def createUserName(self):
        userNameSet = True
        passWordSet = False
        while userNameSet == True:
            userNameInput = input("Please input your new username: ")
            self.c.execute("SELECT * FROM applicantLogin")
            usernames = {username[0] for username in self.c.fetchall()}
            if userNameInput in usernames:
                print("This username has been taken, please try again.")
            else:
                print("Username acceptable")
                userNameSet = False;
                passWordSet = True;

        while passWordSet == True:
            passwordInput = input("Please type in your new password: ")
            print("Username: " + userNameInput + " Password: " + passWordInput)
            print("Are you okay with your new username and password?")
            confirmation = input("1 - Yes, 2 - No: ")

            if(confirmation == "1"):
                self.c.execute("INSERT INTO applicantLogin VALUES(userNameInput, passWordInput)")
                self.conn.commit()
                passWordSet = False

            elif(confirmation == "2"):
                userNameSet = True

        return None

    def closeDataBase(self):
        self.c.close()
        self.conn.close()  

    #def retrieveApplication(str, dict):
#self.c.execute("INSERT INTO HR VALUES ('Bachelor in Computing Science', 'CoventryUniversity', 'Computing Science', 'A', '2021')")


#self.c.execute("""CREATE TABLE Personal_Detail (
#Name text NOT NULL,
#NRIC_Passport text NOT NULL,
#Address text NOT NULL,
#Postcode text NOT NULL,
#Email text NOT NULL,
#PhoneNo text NOT NULL,
#MobileNo text NOT NULL,
#DateOfBirth text NOT NULL,
#Gender text NOT NULL
#ID INT AUTO_INCREMENT PRIMARY KEY,
#)""")

#self.c.execute("""CREATE TABLE Qualifications (
#ID INT AUTO_INCREMENT PRIMARY KEY,
#Qualification text NOT NULL,
#Institution_University text NOT NULL,
#Major text NOT NULL,
#Grade text NOT NULL,
#Year Graduated text NOT NULL
#)""")

#self.c.execute("""CREATE TABLE Working_Experiences (
#ID INT AUTO_INCREMENT PRIMARY KEY,
#Company text NOT NULL,
#Industry text NOT NULL,
#Position text NOT NULL,
#From text NOT NULL,
#To text NOT NULL,
#Level INTEGER NOT NULL,
#Monthly Salary REAL NOT NULL
#)""")

#self.c.execute("""CREATE TABLE References (
#ID INT AUTO_INCREMENT PRIMARY KEY,
#Name text NOT NULL,
#Occupation text NOT NULL,
#Company_Organization text NOT NULL,
#ContactNo text NOT NULL,
#Email text NOT NULL,
#Relationship INTEGER NOT NULL
#)""")

#self.c.execute("""CREATE TABLE HR (
#ID INT AUTO_INCREMENT PRIMARY KEY,
#Date_Received text NOT NULL,
#HR_Officer text NOT NULL,
#Outcome text NOT NULL,
#Reason text NOT NULL,
#Date text NOT NULL
#)""")

#self.c.execute("""CREATE TABLE ApplicantLogin (
#ID text PRIMARY KEY,
#Password text NOT NULL
#)""")
   
#self.c.execute("""CREATE TABLE HRLogin (
#ID text PRIMARY KEY,
#Password text NOT NULL
#)""")

#post a new job application
#allow job applicant to accept for job
#reviewing the job application