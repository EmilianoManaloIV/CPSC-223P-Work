#Emiliano Panday Manalo IV
#02/10/2026
#To Drive The primary logic of the program

#Inport required functions
from contacts import *

#Provide an empty contact list
contact_list = []
#Create a default variables
current_input = -1
#Provide the main logic for the menu system
while current_input != 7:
    #Print the header for the menu
    print("                                     ")
    print("      *** EMPOLOYEE CONTACT MAIN MENU")
    print("                                     ")
    print("1. Print List")
    print("2. Add Contact")
    print("3. Modify Contact")
    print("4. Delete Contact")
    print("5. Sort List By First Name")
    print("6. Sort List By Last Name")
    print("7. Exit The Program")
    print("                                     ")
    #Prompt the user for input menu choice
    current_input = int(check_if_input_null_or_not_digit(input("Enter Menu Choice: ")))
    is_list_empty = check_if_empty(contact_list)
    #Impliment core logic of the menu
    if(current_input == 1):
        #Check if the value is not empty then print
        if(is_list_empty == False):
            print_list(contact_list)
    elif(current_input == 2):
        #Add a new contact into the list
        FN = input("Enter First Name: ")
        LN = input("Enter Last Name: ")
        #Add the contact
        add_contact(contact_list, first_name=FN, last_name=LN)
    elif(current_input == 3):
        #Prompt user for input
        index_to_modify = int(check_if_input_null_or_not_digit(input("Enter The Index Number: ")))
        FN = input("Enter First Name: ")
        LN = input("Enter Last Name: ")
        #Apply and check if its valid
        if(modify_contact(contact_list,first_name=FN,last_name=LN,index=index_to_modify) == False):
            print("Invalid Index Number.")
    elif(current_input == 4):
        #Prompt the user for input
        index_to_delete = int(check_if_input_null_or_not_digit(input("Enter The Index Number: ")))
        #Apply the deletion if valid
        if(delete_contact(contact_list, index = index_to_delete) == False):
            print("Invalid Index Number.")
    elif(current_input == 5):
        sort_contacts(contact_list, column=0)
    elif(current_input == 6):
        sort_contacts(contact_list, column=1)
    elif(current_input == 7):
        break
    else:
        print("Invalid Input! Try Again!")






