from people import *
#Driver database
faculty = []
students = []
#Error handling functions
#FUNCTION: check_if_null
#D: Checks and reprompts if value is empty
def check_if_null(user_input):
    while not user_input or user_input.strip() == "":
        user_input = input("ERROR: VALUE IS EMPTY! PLEASE TRY AGAIN: ")
    return user_input
#FUNCTION: check_if_int
#D: Checks and reprompts if its not an integer
def check_if_int(user_input):
    while True:
        try:
            intInput = int(user_input)
            return intInput
        except (TypeError, ValueError):
            user_input = input("ERROR: VALUE IS NOT AN INTEGER! PLEASE TRY AGAIN: ")
#FUNCTION: check_if_index_exists(user_input, list_being_tested)
#D: Checks if the element exists within the list
def check_if_index_exists(user_input, list_being_tested):
    while True:
        try:
            existingElement = list_being_tested[user_input]
            return existingElement
        except IndexError:
            user_input = input("ERROR: INDEX DOESN'T EXIST! PLEASE TRY AGAIN!: ")
#FUNCTION: display_prompt
#D: Displays the CLI prompt for this program
def display_prompt():
    print('\n\t\t*** TUFFY TITAN STUDENT/FACULTY MAIN MENU\n')
    print('1. Add Faculty\n2. Print Faculty\n3. Add Student\n4. Print Student\n9. Exit The Program\n')
#FUNCTION: display_faculty_header
#D: Displays the CLI header for faculty
def display_faculty_header():
    print('==================== FACULTY ============================')
    print(f'{"Record":<9}{"Name":<23}{"Department":<25}')
    print(f'{"":=<8} {"":=<22} {"":=<25}')
#FUNCTION: display_student_header
#D: Displays the CLI header for Students
def display_student_header():
    print('===================================== STUDENTS ======================================')
    print(f'{"Name":<22}{"Class":<11}{"Major":<27}{"Advisor":<25}')
    print(f'{"":=<22}{"":=<11}{"":=<27}{"":=<25}')
#FUNCTION: display_faculty
#D: Displays all the faculty
def display_faculty(*, faculty_list):
    for index, faculty in enumerate(faculty_list):
        print(f'{index:<9}{faculty.m_firstname + " " + faculty.m_lastname:<23}{faculty.m_department:<25}')
#FUNCTION: display_students
#D: Display all the students in the database
def display_students(*, student_list):
    for Student in student_list:
        print(f'{Student.m_firstname + " " + Student.m_lastname:<22}{Student.m_classyear:<11}{Student.m_major:<27}{Student.m_advisor.m_firstname + " " + Student.m_advisor.m_lastname:<25}')

#FUNCTION: add_faculty
#D: Prompts for faculty details and returns a faculty object
def add_faculty():
    firstName = check_if_null(input("Enter First Name: "))
    lastName = check_if_null(input("Enter Last Name: "))
    department = check_if_null(input("Enter Department: "))
    return Faculty(firstName,lastName,department)
#FUNCTION: add_student
#D: Prompts for student details and returns a student object
def add_student(*,faculty_list):
    firstName = check_if_null(input("Enter First Name: "))
    lastName = check_if_null(input("Enter Last Name: "))
    newStudent = Student(firstName,lastName)
    #classYear = check_if_null(input("Enter Class Year: "))
    #major =  check_if_null(input("Enter Major: "))
    #advisorId = check_if_null(input("Enter Faculty Advisor: "))
    newStudent.set_class(check_if_null(input("Enter Class Year: ")))
    newStudent.set_major(check_if_null(input("Enter Major: ")))
    newStudent.set_advisor(check_if_index_exists(check_if_int(check_if_null(input("Enter Faculty Advisor: "))),faculty_list))
    return newStudent



#FUNCTION: main
#D: Drives the main branch of the program
def main():
    user_input = -1
    while user_input != 9:
        display_prompt()
        user_input = check_if_int(check_if_null(input("Enter Menu Choice: ")))
        if(user_input == 1):
            faculty.append(add_faculty())
        elif(user_input == 2):
            display_faculty_header()
            display_faculty(faculty_list=faculty)
        elif(user_input == 3):
            students.append(add_student(faculty_list=faculty))
        elif(user_input == 4):
            display_student_header()
            display_students(student_list=students)
        else:
            if (user_input != 9):
                print("ERROR: INVALID INPUT! TRY AGAIN!")

if __name__ == "__main__":
    main()



