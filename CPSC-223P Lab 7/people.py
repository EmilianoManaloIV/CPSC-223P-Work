#CLASS: Person
#D: Base class with a first and last name
class Person:
    def __init__(self, first_name, last_name):
        self.m_firstname = first_name
        self.m_lastname = last_name
#CLASS: Faculty(Person)
#D: Faculty that adds department to person class
class Faculty(Person):
    def __init__(self, first_name, last_name, department):
        Person.__init__(self, first_name,last_name)
        self.m_department = department
#CLASS: Student(Person)
#D: Student that adds other student functions to a class
class Student(Person):
    def __init__(self, first_name, last_name):
        Person.__init__(self, first_name, last_name)

    def set_class(self, class_year):
        self.m_classyear = class_year

    def set_major(self, major):
        self.m_major = major

    def set_advisor(self, faculty):
        self.m_advisor = faculty