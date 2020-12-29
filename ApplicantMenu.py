import os
from datetime import date

class ApplicantMenu(object):

    def __init__(self,DB):
        self.DB = DB

    def createNewApplication(self):
        
        newApplicationMenuState = 'NewApplicationMainMenuState'
        newApplicationMenu = True

        jobApplyDict = {'PositionApplied':'', 'DateApplied':'', 'ExpectedSalary': '', 'Availability': '', 'AcceptJob': '', 'ConfirmJob': ''}
        personalDetailDict = {'Name':'', 'NRIC_Passport':'', 'Address':'', 'PostalCode': '', 'Email': '', 'HomeNo': '', 'MobileNo': '', 'DateOfBirth': '', 'Gender': ''}
        qualificationDict = {'Qualification': '', 'InstitutionUniversity': '', 'Major': '', 'Grade': '', 'YearGraduated': ''}
        workingExperienceDict = {'Company': '', 'Industry': '', 'Position': '', 'FromMonth': '', 'FromYear': '', 'ToMonth': '', 'ToYear': '','Level': '', 'MonthlySalary': ''}
        referenceDict = {'Name': '', 'Occupation': '', 'CompanyOrganization': '', 'ContactNo': '', 'Email': '', 'Relationship': ''}

        today = date.today()

        while newApplicationMenu == True:
            if newApplicationMenuState == 'NewApplicationMainMenuState':
                print('____________________________________________')
                print('1. Job Choice')
                print('2. Personal Details')
                print('3. Qualifications')
                print('4. Working Experiences')
                print('5. References')
                print('6. Submit Application')
                print('7. Go Back')
                optionChosen = input("Select option here: ")
                if optionChosen == "1":
                    newApplicationMenuState = 'JobChoiceState'
                elif optionChosen == "2":
                    newApplicationMenuState = 'PersonalDetailState'
                elif optionChosen == "3":
                    newApplicationMenuState = 'QualificationState'
                elif optionChosen == "4":
                    newApplicationMenuState = 'WorkingExperienceState'
                elif optionChosen == "5":
                    newApplicationMenuState = 'ReferenceState'
                elif optionChosen == "6":
                    newApplicationMenuState = 'FinalConfirmationState'
                elif optionChosen == "7":
                    newApplicationMenu = False;
                else:
                    print("Incorrect input, please try again.")

            elif newApplicationMenuState == 'JobChoiceState':
                jobChoiceMenuState = 'PositionState'
                while jobChoiceMenuState != 'ConfirmedState':
                    if jobChoiceMenuState == 'PositionState':
                        jobApplyDict['PositionApplied'] = input("Enter your preferred job position: ")
                        jobChoiceMenuState = 'SalaryState'

                    elif jobChoiceMenuState == 'SalaryState':
                        jobApplyDict['ExpectedSalary'] = input("Enter your expected salary: ")
                        jobChoiceMenuState = 'AvailbilityState'

                    elif jobChoiceMenuState == 'AvailbilityState':
                        jobApplyDict['Availability'] = input("Enter the number of months you are available: ")
                        jobChoiceMenuState = 'CheckState'

                    elif jobChoiceMenuState == 'CheckState':
                        confirmation = input("Are you sure about your input?\n1 - Yes, 2 - No: ")
                        if confirmation == "1":
                            jobApplyDict['Date'] = today.strftime("%d/%m/%Y")
                            jobApplyDict['AcceptJob'] = "0"
                            jobApplyDict['ConfirmJob'] = "0"
                            jobChoiceMenuState = 'ConfirmedState'
                        elif confirmation == "2":
                            jobChoiceMenuState = 'PositionState'
                        else:
                            print("Incorrect input, please try again.")
                else:
                    newApplicationMenuState = 'NewApplicationMainMenuState'

            elif newApplicationMenuState == 'PersonalDetailState':
                personalDetailMenuState = 'NameState'
                while personalDetailMenuState != 'ConfirmedState':
                    if personalDetailMenuState == 'NameState':
                        personalDetailDict['Name'] = input("Enter the applicant's name: ")
                        personalDetailMenuState = 'NRICState'

                    elif personalDetailMenuState == 'NRICState':
                        personalDetailDict['NRIC_Passport'] = input("Enter your NRIC or Passport No: ")
                        personalDetailMenuState = 'AddressState'

                    elif personalDetailMenuState == 'AddressState':
                        personalDetailDict['Address'] = input("Enter your home address: ")
                        personalDetailMenuState = 'PostCodeState'

                    elif personalDetailMenuState == 'PostCodeState':
                        personalDetailDict['PostalCode'] = input("Enter your postal code: ")
                        personalDetailMenuState = 'EmailState'

                    elif personalDetailMenuState == 'EmailState':
                        personalDetailDict['Email'] = input("Enter your email: ")
                        personalDetailMenuState = 'HomeNoState'

                    elif personalDetailMenuState == 'HomeNoState':
                        personalDetailDict['HomeNo'] = input("Enter your home number: ")
                        personalDetailMenuState = 'MobileNoState'

                    elif personalDetailMenuState == 'MobileNoState':
                        personalDetailDict['MobileNo'] = input("Enter your mobile number: ")
                        personalDetailMenuState = 'DateOfBirthState'

                    elif personalDetailMenuState == 'DateOfBirthState':
                        dateOfBirth = input("Enter the day of your Birth: ")
                        monthOfBirth = input("Enter the month of your Birth: ")
                        yearOfBirth = input("Enter the year of your Birth: ")
                        personalDetailDict['DateOfBirth'] = dateOfBirth + "/" + monthOfBirth + "/" + yearOfBirth
                        personalDetailMenuState = 'GenderState'

                    elif personalDetailMenuState == 'GenderState':
                        genderInput = input("Select your gender:\n1 - Male 2 - Female: ")
                        if genderInput == '1':
                            personalDetailDict['Gender']  = 'Male'
                            personalDetailMenuState = 'CheckState'
                        elif genderInput == '2':
                            personalDetailDict['Gender']  = 'Female'
                            personalDetailMenuState = 'CheckState'
                        else:
                            print("Please enter 1 or 2 only.")

                    elif personalDetailMenuState == 'CheckState':
                        confirmation = input("Are you sure about your application?\n1 - Yes, 2 - No: ")
                        if confirmation == '1':
                            personalDetailMenuState = 'ConfirmedState'
                        elif confirmation == '2':
                            personalDetailMenuState = 'GenderState'
                        else:
                            print("Incorrect input, please try again.")
                else:
                    newApplicationMenuState = 'NewApplicationMainMenuState'

            elif newApplicationMenuState == 'QualificationState':
                qualificationMenuState = 'QualificationState'
                while qualificationMenuState != 'ConfirmedState':
                    if qualificationMenuState == 'QualificationState':
                        qualificationDict['Qualification'] = input("Enter your qualification: ")
                        qualificationMenuState = 'InstitutionUniState'

                    elif qualificationMenuState == 'InstitutionUniState':
                        qualificationDict['InstitutionUniversity'] = input("Enter the Institution or University you've studied in: ")
                        qualificationMenuState = 'MajorState'

                    elif qualificationMenuState == 'MajorState':
                        qualificationDict['Major'] = input("Enter your Major: ")
                        qualificationMenuState = 'GradeState'

                    elif qualificationMenuState == 'GradeState':
                        qualificationDict['Grade'] = input("Enter your GPA that you've obtained: ")
                        qualificationMenuState = 'YearGraduateState'

                    elif qualificationMenuState == 'YearGraduateState':
                        qualificationDict['YearGraduated'] = input("Enter the year you've graduated: ")
                        qualificationMenuState = 'CheckState'

                    elif qualificationMenuState == 'CheckState':
                        confirmation = input("Are you sure about your input?\n1 - Yes, 2 - No: ")
                        if confirmation == "1":
                            qualificationMenuState = 'ConfirmedState'
                        elif confirmation == "2":
                            qualificationMenuState = 'PositionState'
                        else:
                            print("Incorrect input, please try again.")
                else:
                    newApplicationMenuState = 'NewApplicationMainMenuState'

            elif newApplicationMenuState == 'WorkingExperienceState':
                workingExperienceMenuState = 'CompanyState'
                while workingExperienceMenuState != 'ConfirmedState':
                    if workingExperienceMenuState == 'CompanyState':
                        workingExperienceDict['Company'] = input("Enter the name of the company you worked in: ")
                        workingExperienceMenuState = 'IndustryState'

                    elif workingExperienceMenuState == 'IndustryState':
                        workingExperienceDict['Industry'] = input("Enter the name of the industry of the company: ")
                        workingExperienceMenuState = 'PositionState'

                    elif workingExperienceMenuState == 'PositionState':
                        workingExperienceDict['Position'] = input("Enter your position in the job: ")
                        workingExperienceMenuState = 'FromDateState'

                    elif workingExperienceMenuState == 'FromDateState':
                        fromMonth = input("Enter the month when you started: ")
                        fromYear = input("Enter the year when you started: ")
                        workingExperienceDict['FromDate'] = fromMonth + "/" + fromYear
                        workingExperienceMenuState = 'ToDateState'

                    elif workingExperienceMenuState == 'ToDateState':
                        ToMonth = input("Enter the month when you started: ")
                        ToYear = input("Enter the year when you started: ")
                        workingExperienceDict['ToDate'] = ToMonth + "/" + ToYear
                        workingExperienceMenuState = 'LevelState'

                    elif workingExperienceMenuState == 'LevelState':
                        workingExperienceDict['Level'] = input("Enter your job position level: ")
                        workingExperienceMenuState = 'SalaryState'

                    elif workingExperienceMenuState == 'SalaryState':
                        workingExperienceDict['MonthlySalary'] = input("Enter the monthly salary for that job: ")
                        workingExperienceMenuState = 'CheckState'

                    elif workingExperienceMenuState == 'CheckState':
                        confirmation = input("Are you sure about your input?\n1 - Yes, 2 - No: ")
                        if confirmation == "1":
                            workingExperienceMenuState = 'ConfirmedState'
                        elif confirmation == "2":
                            workingExperienceMenuState = 'CompanyState'
                        else:
                            print("Incorrect input, please try again.")
                else:
                    newApplicationMenuState = 'NewApplicationMainMenuState'

            elif newApplicationMenuState == 'ReferenceState':
                referenceMenuState = 'NameState'
                while referenceMenuState != 'ConfirmedState':
                    if referenceMenuState == 'NameState':
                        referenceDict['Name'] = input("Enter the name of the person being referred: ")
                        referenceMenuState = 'OccupationState'

                    elif referenceMenuState == 'OccupationState':
                        referenceDict['Occupation'] = input("Enter the occupation of the referred person: ")
                        referenceMenuState = 'CompanyState'

                    elif referenceMenuState == 'CompanyState':
                        referenceDict['CompanyOrganization'] = input("Enter the company the referred person works at: ")
                        referenceMenuState = 'ContactNoState'

                    elif referenceMenuState == 'ContactNoState':
                        referenceDict['ContactNo'] = input("Enter the contact number of the referred person: ")
                        referenceMenuState = 'EmailState'

                    elif referenceMenuState == 'EmailState':
                        referenceDict['Email'] = input("Enter the email of the referred person: ")
                        referenceMenuState = 'relationshipState'

                    elif referenceMenuState == 'relationshipState':
                        referenceDict['Relationship'] = input("Enter your relationship to this referred person: ")
                        referenceMenuState = 'CheckState'

                    elif referenceMenuState == 'CheckState':
                        confirmation = input("Are you sure about your input?\n1 - Yes, 2 - No: ")
                        if confirmation == "1":
                            referenceMenuState = 'ConfirmedState'
                        elif confirmation == "2":
                            referenceMenuState = 'PositionState'
                        else:
                            print("Incorrect input, please try again.")
                else:
                    newApplicationMenuState = 'NewApplicationMainMenuState'

            elif newApplicationMenuState == 'FinalConfirmationState':
                finalConfirmation = input("Are you sure about submitting your application?\n1 - Yes, 2 - No: ")
                if finalConfirmation == "1":
                    dictList = [jobApplyDict, personalDetailDict, qualificationDict, workingExperienceDict, referenceDict]
                    self.DB.submitNewApplication(dictList)
                    newApplicationMenu = False;
                elif confirmation == "2":
                    newApplicationMenuState = 'NewApplicationMainMenuState'
                else:
                    print("Incorrect input, please try again.")
                


    @staticmethod
    def reviewSubmittedApplication(self):

        reviewApplicationMenuState = 'ReviewState'

        while reviewApplicationMenuState != 'ConfirmedState':

            if reviewApplicationMenuState == 'ReviewState':
                print("Shoot")

            elif reviewApplicationMenuState == 'ReviewState':
                print('Potato')

        else:
            return None
        

