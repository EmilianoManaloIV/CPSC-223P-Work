from contacts import *


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
#FUNCTION: display_prompt
#D: Displays the CLI prompt for this program
def display_prompt():
    print('\n\t\t*** TUFFY TITAN CONTACT MAIN MENU\n')
    print('1. Add Contact')
    print('2. Modify Contact')
    print('3. Delete Contact')
    print('4. Print Contact List')
    print('5. Set Contact Filename')
    print('6. Exit The Program\n')
#FUNCTION: display_contact_header
#D: Displays the CLI header for contacts
def display_contact_header():
    print('==================== CONTACT LIST ====================')
    print(f'{"Last Name":<21}{"First Name":<22}{"Phone":<11}')
    print(f'{"":=<20} {"":=<21} {"":=<10}')
#FUNCTION: main
#D: Heart main driver of the program
def main():
    contact = Contact(filename="ContactData")
    user_input = -1
    attemptedInput = None
    while user_input != 6:
        display_prompt()
        user_input = check_if_int(check_if_null(input("Enter Menu Choice: ")))
        if(user_input == 1):
            attemptedInput = contact.add_contact(id=check_if_null(input("Enter Phone Number: ")),
                                   first_name=check_if_null(input("Enter First Name: ")),
                                   last_name=check_if_null(input("Enter Last Name: ")))
            if(attemptedInput == "error"):
                continue
            else:
                for name in attemptedInput.values():
                    print(f'Added: {name[0]} {name[1]}')
        elif(user_input == 2):
            attemptedInput = contact.modify_contact(id=check_if_null(input("Enter Phone Number: ")),
                                                 first_name=check_if_null(input("Enter First Name: ")),
                                                 last_name=check_if_null(input("Enter Last Name: ")))
            if (attemptedInput == "error"):
                continue
            else:
                for name in attemptedInput.values():
                    print(f'Modified: {name[0]} {name[1]}')
        elif(user_input == 3):
            attemptedInput = contact.delete_contact(id=check_if_null(input("Enter Phone Number: ")))
            if (attemptedInput == "error"):
                continue
            else:
                for name in attemptedInput.values():
                    print(f'Deleted: {name[0]} {name[1]}')
        elif(user_input == 4):
            display_contact_header()
            for phone, name in contact.dictionary.items():
                print(f'{name[1]:<20} {name[0]:<21} {phone:<10}')
        elif(user_input == 5):
            contact = Contact(filename=check_if_null(input("Set Contact File Name: ")))
        else:
            if(user_input != 6):
                print("ERROR: INVALID INPUT! TRY AGAIN!")
if __name__ == "__main__":
    main()