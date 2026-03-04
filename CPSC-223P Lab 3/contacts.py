#NAME: Emiliano Manalo
#DATE: 02/17/2026
#PURPOSE: To create an employee database using dictionaries

#FUNCTION: add_contact(employee_dictionary, employee_id, first_name, last_name)
#PURPOSE: To add a new contact given a prompt
def add_contact(contact_dictionary, /, *, contact_id, first_name, last_name):
    """Adds A Contact With First And Last Name"""
    # Create a new list utilizing the prompt and given data
    new_entry = [first_name, last_name]
    returned_value = None
    # Check if the element already exists
    if contact_id in contact_dictionary:
        print("ERROR! CONTACT ALREADY EXISTS!")
    else:
        contact_dictionary[contact_id] = new_entry
        returned_value = new_entry
    return returned_value

#FUNCTION: modify_contact(employee_dictionary, employee_id, first_name, last_name)
#PURPOSE: To modify an existing list at a certain index
def modify_contact(contact_dictionary, /, *, contact_id, first_name, last_name):
    """Modified An Existing Contact With A Given ID"""
    returned_value = None
    #Check if the index is valid
    if contact_id not in contact_dictionary:
        print("ERROR! CONTACT DOESN'T EXIST!")
    else:
        new_entry = [first_name, last_name]
        contact_dictionary[contact_id] = new_entry
        returned_value = new_entry
    return returned_value

#FUNCTION: delete_contact(contact_dictionary,/,*,contact_id)
#PURPOSE: To delete a contact list if the index exists
def delete_contact(contact_dictionary, /, *, contact_id):
    """Deletes A Contact With A Valid Index"""
    return_value = None
    #Check if the given index is valid
    if contact_id not in contact_dictionary:
        print("ERROR! CONTACT DOESN'T EXIST!")
    else:
        return_value = contact_dictionary.pop(contact_id)
    return return_value

#FUNCTION: sort_contacts(contact_dictionary,/,*,)
#PURPOSE: To sort a given list if you want something based on
#first name or last name
def sort_contacts(contact_dictionary,/,):
    """Sorts Contacts Based On Last Name Then First Name"""
    sorted_contact_dictionary = sorted(contact_dictionary.items(), key=lambda x: x[1][1])
    sorted_contact_dictionary = sorted(sorted_contact_dictionary, key=lambda x: x[1][0])
    return sorted_contact_dictionary

#FUNCTION: find_contact(contact_dictionary,/,*,find)
#PURPOSE: To find a certain contact within the dictionary
def find_contact(contact_dictionary,/,*,find):
    """Returns A Dictionary Of Found ID"""
    #Create an empty dictionary
    return_value = {}
    if find in contact_dictionary:
        return_value[find] = contact_dictionary[find]
    for contact in contact_dictionary.items():
        if find.lower() == contact[1][0].lower() or find.lower() == contact[1][1].lower():
            first_name = contact[1][0]
            last_name = contact[1][1]
            return_value[contact[0]] = [first_name,last_name]
    return sort_contacts(return_value)

#Modified functions for a dictionary

#FUNCTiON: check_if_empty(A list argument)
#PURPOSE: To check if a list is empty or not
def check_if_empty(contact_dictionary):
    if contact_dictionary == {}:
        print("WARNING: DICTIONARY IS EMPTY! PLEASE ADD A CONTACT!")
        return True
    else:
        return False

#FUNCTION: check_if_input_null(Some String Input)
#PURPOSE: Dictates of certain inputs such as empty inputs or not numeric
def check_if_input_null_or_not_digit(input_to_check):
    if not input_to_check:
        print("WARNING: VALUE IS NULL! ASSIGNING DEFAULT VALUE!")
        input_to_check = -1
    elif input_to_check.isdigit() == False:
        print("WARNING: VALUE IS NOT A DIGIT! ASSIGNING DEFAULT VALUE!")
        input_to_check = -2
    return input_to_check