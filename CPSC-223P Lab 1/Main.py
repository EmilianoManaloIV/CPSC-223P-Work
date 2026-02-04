#Emiliano Panday Manalo IV
#02/03/2026
#To Drive The Main Logic Of The Program

#Import required functions
from contacts import *

#Provide an empty contact list
contact_list = []
#Create a default variable
current_input = -1
#Create the main logic for the menu system:
while current_input != 5:
    #Print the header for the menu
    print("                                     ")
    print("      *** EMPOLOYEE CONTACT MAIN MENU")
    print("                                     ")
    print("1. Print List")
    print("2. Add Contact")
    print("3. Modify Contact")
    print("4. Delete Contact")
    print("5. Exit The Program")
    print("                                     ")
    #Prompt the user of a menu choice
    current_input = int(check_if_input_null_or_not_digit(input("Enter Menu Choice: ")))
    is_list_empty = check_if_empty(contact_list)
    #Impliment logical operation based on menu choice
    if(current_input == 1 and is_list_empty == False):
        print_list(contact_list)
    elif(current_input == 2):
        contact_list = add_contact(contact_list)
    elif(current_input == 3 and is_list_empty == False):
        contact_list = modify_contact(contact_list)
    elif(current_input == 4 and is_list_empty == False):
        contact_list = delete_contact(contact_list)
    elif(current_input == 5):
        break
    else:
        print("Invalid Input! Try Again!")





