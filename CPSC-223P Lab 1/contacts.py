#Emiliano Panday Manalo IV
#01/29/2026
#Set the primary functions used in this contact program

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
    #if not ori_list:
        #print("================== EMPTY LIST ====================")
    #else:
        #for i in range(len(ori_list)):
            #print(f'{str(i):8}{ori_list[i][0]:22}{ori_list[i][1]:22}')
    for i in range(len(ori_list)):
        print(f'{str(i):8}{ori_list[i][0]:22}{ori_list[i][1]:22}')
#TEST_1: Determine if display function is working correctly
#print_list([["Richard", "Stallman"],["First_Name", "Last Name"]])

#FUNCTION: add_contact(list of list argument)
#PURPOSE: To add a new contact to list using a prompt
def add_contact(ori_list):
    """Adds A New Contact To A Given list"""
    #Prompt and add first and last name
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    #Create a new list utilizing the prompt and given data
    new_entry = [first_name, last_name]
    #Add the new element to the list
    ori_list.append(new_entry)
    #Return the new updated list
    return ori_list
#TEST: Determine if a new element has been added onto the list
#testList = [["Richard", "Stallman"],["First_Name", "Last Name"]]
#print_list(testList)
#testList = add_contact(testList)
#print_list(testList)

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
#TEST: Determine if the loop works and reprompts
#testList = [["Richard", "Stallman"],["First_Name", "Last Name"]]
#Valid Index
#check_if_valid_index(testList, 1)
#Invalid Index
#check_if_valid_index(testList, 3)

#FUNCTION: modfiy_contact(List Of List Argument)
#PURPOSE: To Modify An Exisiting Element Within The List Of List
def modify_contact(ori_list):
    """Modifies An Exisiting Contact's List Element"""
    #Get the index to modify and check if its valid
    index_to_modify = int(check_if_input_null_or_not_digit(input("Enter The Index Number: ")))
    index_to_modify = check_if_valid_index(ori_list, index_to_modify)
    #Once index is valid, impliment the change
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    #Replace the selected element
    ori_list[index_to_modify][0] = first_name
    ori_list[index_to_modify][1] = last_name
    #Return the modified list
    return ori_list
#TEST: Test if the value is modified and edge cases are addressed
#testList = [["Richard", "Stallman"],["First_Name", "Last Name"]]
#print_list(testList)
#testList = modify_contact(testList)
#print_list(testList)

#FUNCTION: delete_contact(List of Lists argument)
#PURPOSE: To delete a certain contact out of a contact list
def delete_contact(ori_list):
    """Delete A Selected Contact Out Of The Contact List"""
    #Prompt for index and validate if its valid
    index_to_delete = int(check_if_input_null_or_not_digit(input("Enter The Index Number: ")))
    index_to_delete = check_if_valid_index(ori_list, index_to_delete)
    #If valid, delete that element out of the list
    del ori_list[index_to_delete]
    #Return the modified list
    return ori_list
#TEST: Make sure that it deletes the proper element and address edge cases
#testList = [["Richard", "Stallman"],["First_Name", "Last Name"]]
#print_list(testList)
#testList = delete_contact(testList)
#print_list(testList)
