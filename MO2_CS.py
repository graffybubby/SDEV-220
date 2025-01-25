# Author: Graftin Gubocki
# Program Name: MO2_CS.py
# Functionality: This application will accept student names and GPAs and 
# test if the student qualifies for either the Dean's List or the Honor Roll.

# helper function to clear the screen quickly using ansi escape codes
def clear():
    print("\033c")

# function to determine if a variable is a float
def isFloat(input):
    try: 
        float(input)
        return True
    except:
        return ValueError

# function to collect and validate user inputs 
def collectValidate():
    running = True
    students = []
    studentNameError = ("Student names must only contain alphabetical characters. Please try again.")
    # begin main function loop
    while(running):
        # set validation variables to true    
        va = True
        vb = True
        vc = True 
        # begin collecting student information starting with last name
        while(va):
            studentLName = input("Please enter the students last name:")
            # if the students last name is 'zzz' cancel further inputs by setting all validation bools to false
            # and stop the main loop by setting 'running' to false
            if studentLName.lower() == "zzz": 
                print("Processing students now...")
                va = False
                vb = False
                vc = False
                running = False
                break
            elif studentLName.isalpha() == False:
                print(studentNameError)
            else: break
        # collect student first name
        while(vb):
            studentFName = input("Please enter the students first name:")
            if studentFName.isalpha() == False:
                print(studentNameError)
            else: vb = False
        # collect student gpa
        while(vc):
            studentGpa = input("Please enter the students GPA:")
            # using previously defined function to validate that the students gpa is a float while
            # avoiding using float(input(...)) so the console doesnt give an unsightly error message upon incorrect input type
            if isFloat(studentGpa):
                vc = False
            else: print("Student GPA must maintain this structure '0.00'. Please try again.")
        # packing collected and validated inputs into a tuple 
        studentInfo = (studentLName, studentFName, float(studentGpa))
        # if the students last name is 'zzz' do not append further data into the student list
        if studentInfo[0] != "zzz":
            # append valid student information into a list 
            students.append(studentInfo)
    return students  
      
# function finding which students made dean's list or honor roll, accepts list of students