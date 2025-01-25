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
                print("\nProcessing students now...")
                va = False
                vb = False
                vc = False
                running = False
                break
            # confirm students last name contains only alphabetical characters
            elif studentLName.isalpha() == False:
                print(studentNameError)
            else: break
        # collect student first name
        while(vb):
            studentFName = input("Please enter the students first name:")
            # confirm students first name contains only alphabetical characters
            if studentFName.isalpha() == False:
                print(studentNameError)
            else: vb = False
        # collect student gpa
        while(vc):
            studentGpa = input("Please enter the students GPA:")
            # using previously defined function to validate that the students gpa is a float while
            # avoiding using float(input(...) so the console doesnt give an unsightly error message upon incorrect input type
            if isFloat(studentGpa) and studentGpa > 0:
                vc = False
            else: print("Student GPA must maintain this structure '0.00'. Please try again.")
        # packing collected and validated inputs into a tuple 
        studentInfo = (studentLName, studentFName, float(studentGpa))
        # if the students last name is 'zzz' do not append further data into the students list
        if studentInfo[0] != "zzz":
            # append valid student information into the students list 
            students.append(studentInfo)
    return students  
      
# function finding which students made dean's list or honor roll, accepts list of students.
def placement(students):
    deans = []
    honor = []
    for student in students:
        FName, LName, Gpa = student
        # if a students gpa is 3.5 or greater, add them to the dean's list list
        if Gpa >= 3.5:
            deans.append(student)
        # if a students gpa is less than 3.5 but greater than 3.25, add them to the honor roll
        elif Gpa >= 3.25 and Gpa < 3.5:
            honor.append(student)
    # pack honor roll and dean's list lists into a tuple
    hdcombo = (honor, deans)
    return hdcombo

# function displaying the students from honor roll and deans list, accepts tuple of lists (honor roll and dean's list).
def displayData(hdcombo):
    # unpack tuple containing the honor roll and dean's list
    honor, deans = hdcombo
    print("\nHonor roll students:")
    # if the honor roll list contains any elements (students), display them.
    if len(honor) != 0:
        # iterate through honor roll list
        for student in honor:
            # unpack each student's tuple on honor roll
            Lname, Fname, Gpa = student
            print("Name: ", Fname, " ", Lname, " | GPA: ", Gpa)
    else: print("    There are no students on the Honor roll.")

    print("\nDean's list students:")
    # if the dean's list contains any elements (students), display them.
    if len(deans) != 0:
        # iterate through the dean's list list
        for student in deans:
            # unpack each student's tuple on the dean's list
            Lname, Fname, Gpa = student
            print("Name: ", Fname, " ", Lname, " | GPA: ", Gpa)
    else: print("    There are no students on the Dean's list.")

# main function
def main():
    clear()
    students = placement(collectValidate()) 
    displayData(students)

main()
        

    


