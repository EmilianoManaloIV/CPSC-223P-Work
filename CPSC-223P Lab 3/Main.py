#NAME: Emiliano Manalo
#DATE: 02/17/2026
#To Drive The primary logic of the program

#Inport required functions
from contacts import *

#Provide an empty contact list
contact_dictionary = {}
#Create a default variables
current_input = -1
#Provide the main logic for the menu system
while current_input != 7:
    #Print the header for the menu
    print("                                     ")
    print("      *** EMPOLOYEE CONTACT MAIN MENU")
    print("                                     ")
    print("1. Add Contact")
    print("2. Modify Contact")
    print("3. Delete Contact")
    print("4. Print Contact List")
    print("5. Find Contact")
    print("6. Exit The Program")
    print("                                     ")
    #Prompt the user for input menu choice
    current_input = int(check_if_input_null_or_not_digit(input("Enter Menu Choice: ")))
    #Impliment core logic of the menu
    if current_input == 1:
        phone_number = input("Enter Phone Number: ")
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        added = add_contact(contact_dictionary, contact_id = phone_number, first_name=first_name, last_name=last_name)
        if added == None:
            print("Phone Number Already Exists!")
        else:
            print("Added: " + added[0] + " " + added[1])
    elif current_input == 2:
        phone_number = input("Enter Phone Number: ")
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        modified = modify_contact(contact_dictionary, contact_id=phone_number,first_name=first_name,last_name=last_name)
        if modified == None:
            print("Phone Number Doesn't Exist!")
        else:
            print("Modified: " + modified[0] + " " + modified[1])
    elif current_input == 3:
        phone_number = input("Enter Phone Number: ")
        removed = delete_contact(contact_dictionary,contact_id=phone_number)
        if removed == None:
            print("Phone Number Doesn't Exist!")
        else:
            print("Deleted: " + removed[0] + " " + removed[1])
    elif current_input == 4:
        # Display the header for the contact list
        print("==================== CONTACT LIST ====================")
        print("Last Name             First Name            Phone")
        print("====================  ====================  ==========")
        for contacts in contact_dictionary.items():
            print(f'{contacts[1][1]:22}{contacts[1][0]:22}{contacts[0]}')
    elif current_input == 5:
        search = input("Enter Search String: ")
        found_contacts = find_contact(contact_dictionary,find = search)
        print("==================== FOUND CONTACT(S) ================")
        print("Last Name             First Name            Phone")
        print("====================  ====================  ==========")
        for contacts in found_contacts:
            print(f'{contacts[1][1]:22}{contacts[1][0]:22}{contacts[0]}')
    elif current_input == 6:
        break
    else:
        print("Invalid Input! Try Again!")






