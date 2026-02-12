#NAME: Emiliano Manalo
#DATE: 02/05/2026
#PURPOSE: To add more functionality to the employee contact system

#REUSED FUNCTIONS FROM BEFORE

#FUNCTiON: check_if_empty(A list argument)
#PURPOSE: To check if a list is empty or not
def check_if_empty(list_to_be_tested):
    if not list_to_be_tested:
        print("WARNING: LIST IS EMPTY! PLEASE ADD A CONTACT!")
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

#FUNCTION: print_list(list of list argument)
#PURPOSE: To print the list of contacts
def print_list(ori_list):
    """Prints A Given List With Header Format"""
    #Display the header for the contact list
    print("================== CONTACT LIST ==================")
    print("Index   First Name            Last Name")
    print("======  ====================  ====================")
    #Display the elements in row collumn form and check if there is no data and display response
    for i in range(len(ori_list)):
        print(f'{str(i):8}{ori_list[i][0]:22}{ori_list[i][1]:22}')

#FUNCTION: check_if_valid_index(list argument, index/int argument)
#PURPOSE: To check if the given index is valid for the list given
def check_if_valid_index(list_being_tested, index_being_tested):
    """Checks If The Index Is In Range Of The List"""
    #Set the check condition
    is_valid = False
    #Set the loop that will keep prompting if given invalid indexes
    while is_valid == False:
        #Check if index is valid or not
        if index_being_tested in range(len(list_being_tested)):
            #Return value if valid
            is_valid = True
            return index_being_tested
        else:
            #Prompt the user to input another value that is valid and try again
            print("INVALID INPUT! TRY ANOTHER INDEX!")
            #Make sure to convert into an integer before processing
            index_being_tested = int(check_if_input_null_or_not_digit(input("Enter The Index Number: ")))

#FUNCTION: check_if_valid_index_bool(Given list, given integer index)
def check_if_valid_index_bool(list_being_tested, index_being_tested):
    is_valid = False
    if index_being_tested in range(len(list_being_tested)):
        is_valid = True
    return is_valid
#UPDATED AND REVISED FUNCTIONS

#FUNCTION: add_contact(List of list Args, first_name = stringArg, last_name = stringArg)
#PURPOSE: To add a new contact given a prompt
def add_contact(contact_list,/,*, first_name, last_name):
    """Adds A Contact With First And Last Name"""
    # Create a new list utilizing the prompt and given data
    new_entry = [first_name, last_name]
    # Add the new element to the list
    contact_list.append(new_entry)

#FUNCTION: modify_contact(list of list args, first_name stringArg, last_name = stringArg, index = intArg)
#PURPOSE: To modify an existing list at a certain index
def modify_contact(contact_list,/,*,first_name, last_name, index):
    """Modified An Existing Contact At A Given Index"""
    #Check if the index is valid
    is_valid_index = check_if_valid_index_bool(contact_list, index)
    #If the index is valid
    if is_valid_index == True:
        #Repalace the selected element
        contact_list[index][0] = first_name
        contact_list[index][1] = last_name
    #Return state of index
    return is_valid_index

#FUNCTION: delete_contact(contact_list,/,*,index)
#PURPOSE: To delete a contact list if the index exists
def delete_contact(contact_list,/,*,index):
    """Deletes A Contact With A Valid Index"""
    #Check if the given index is valid
    is_valid_index = check_if_valid_index_bool(contact_list, index)
    if is_valid_index == True:
        del contact_list[index]
    #Return state of index
    return is_valid_index

#FUNCTION: sort_contacts(contact_list,/,*,column)
#PURPOSE: To sort a given list if you want something based on
#first name or last name
def sort_contacts(contact_list,/,*,column):
    """Sorts Contacts Based On First Name Or Last Name"""
    if(column == 0):
        contact_list.sort(key=lambda x: x[0])
    elif(column == 1):
        contact_list.sort(key=lambda x: x[1])
    else:
        print("WARNING: INVALID PARAMETER! NOT DOING ANYTHING!")