#LIBRARY: json
#D: Used to modify json type files
import json
#CLASS: Contact
#D: Seves as an object to manipulate and change a contact list
class Contact:
    # FUNCTION: LoadData
    # D: Loads data into the dictionary
    def load_data(self):
        try:
            with open(self.filename, "r") as fileObject:
                self.dictionary = json.load(fileObject)
        except FileNotFoundError:
            print(f'ERROR: {self.filename} IS NOT FOUND! NO DATA IS LOADED!')
    #FUNCTION SortData
    #D: Sorts data by last name, then first came, then case sensativity
    def sort_data(self):
        self.dictionary = dict(sorted(self.dictionary.items(), key=lambda x: (x[1][1].casefold(), x[1][0].casefold())))
    # FUNCTION: SaveData
    # D: Saves data into dictionary
    def save_data(self):
        try:
            with open(self.filename, "w") as fileObject:
                json.dump(self.dictionary, fileObject)
        except:
            print(f'ERROR: {self.filename} IS NOT FOUND! FILE NOT BEING WRITTEN!')
    # FUNCTION: __init__
    # D: Loads object data from a json file when created
    def __init__(self, /, *, filename):
        self.filename = filename
        self.dictionary = {}
        self.load_data()

    # FUNCTION: add_contact
    # D: Adds a new contact to the dictionary and saves it
    def add_contact(self,/,*,id,first_name,last_name):
        if id in self.dictionary:
            print(f'ERROR: {id} ALREADY EXISTS!')
            return "error"
        self.dictionary[id]=[first_name,last_name]
        self.sort_data()
        self.save_data()
        return {id:[first_name,last_name]}
    #FUNCTION: modify_contact
    #D: Used to modify an already existing contact
    def modify_contact(self,/,*,id,first_name,last_name):
        if id not in self.dictionary:
            print(f'ERROR: {id} NOT FOUND!')
            return 'error'
        self.dictionary[id] = [first_name,last_name]
        self.sort_data()
        self.save_data()
        return {id:[first_name,last_name]}
    #FUNCTION: delete_contact
    #D: Deletes a selected contact
    def delete_contact(self,/,*,id):
         if id not in self.dictionary:
             print(f'ERROR: {id} DOES NOT EXIST!')
             return "error"
         deletedValue = self.dictionary.pop(id)
         self.save_data()
         return {id:deletedValue}
