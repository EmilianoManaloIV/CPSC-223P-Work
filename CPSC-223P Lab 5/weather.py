#Import required packages
import json
import calendar
from pathlib import Path

def weather(*,fileName):
    '''Takes In A fileName and returns a dictionary from a JSON'''
    #Create an empty dictionary
    my_dict = {}
    #Check if file path exists
    file_path = Path(fileName)
    if file_path.exists():
        #If it exists, open and get the contents as a JSON
        with open(fileName, "r") as fileObject:
            my_dict = json.load(fileObject)
    #Else throw an error and return empty dictionary
    else:
        print(f"WARNING: {fileName} NOT FOUND; RETURNING EMPTY DICTIONARY")
    #DEBUG
    #print(my_dict)
    return my_dict

def write_data(*,data,fileName):
    """Takes a data dictionary and filename to write to in JSON format if it exists"""
    #Check if file exists
    file_path = Path(fileName)
    if file_path.exists():
        # If it exists, open and write contents to JSON
        with open(fileName,"w") as fileObject:
            json.dump(data, fileObject)
    #If it doesn't exist do nothing and return an error

def get_related(*,data,date):
    """Returns A Dictionary Only With YYYYMMDD Format"""
    strippedDate =  date[:8]
    relatedData = {k: v for k, v in data.items() if k.startswith(strippedDate)}
    return relatedData

def max_temperature(*,data,date):
    """Provides the max tempeature of a certain day"""
    relatedDictionary = get_related(data=data,date=date)
    return max(entry["t"] for entry in relatedDictionary.values())

def min_temperature(*,data,date):
    """Provides the min tempeature of a certain day"""
    relatedDictionary = get_related(data=data,date=date)
    return min(entry["t"] for entry in relatedDictionary.values())

def max_humidity(*,data,date):
    """Provides the max humidity of a certain day"""
    relatedDictionary = get_related(data=data,date=date)
    return max(entry["h"] for entry in relatedDictionary.values())

def min_humidity(*,data,date):
    """Provides the min humidity of a certain day"""
    relatedDictionary = get_related(data=data,date=date)
    return min(entry["h"] for entry in relatedDictionary.values())

def tot_rain(*,data,date):
    """Provides the total rain for that particular day"""
    relatedDictionary = get_related(data=data, date=date)
    return sum(entry["r"] for entry in relatedDictionary.values())

def report_daily(*,data,date):
    header = (
        "========================= DAILY REPORT ====================\n"
        "Date                     Time Temperature Humidity Rainfall\n"
        "==================== ======== =========== ======== ========\n")
    allLines = []
    for entry in data:
        #print(f"{entry} Incremented")
        if entry.startswith(date[:8]):
            #DEBUG
            #Get time componenets
            entryYear = int(entry[:4])
            entryMonth = int(entry[4:6])
            entryDay = int(entry[6:8])
            entryHour = int(entry[8:10])
            entryMin = int(entry[10:12])
            entrySec = int(entry[12:14])
            fancyDate = f"{calendar.month_name[entryMonth]} {entryDay}, {entryYear}"
            time = f"{entryHour:02d}:{entryMin:02d}:{entrySec:02d}"
            #Get other components
            entryTemp = data[entry]["t"]
            entryHumid = data[entry]["h"]
            entryRain = data[entry]["r"]
            #Format all of the values into one string and then append
            line = f"{fancyDate:<20} {time} {entryTemp:>11} {entryHumid:>8} {entryRain:>8.2f}\n"
            allLines.append(line)
    #Now combine everything into one line
    return header + "".join(allLines)

def report_historical(*,data):
    header = (
        "============================== HISTORICAL REPORT ======================\n"
        "                       Minimum     Maximum  Minumum  Maximum    Total\n"
        "Date                 Temperature Temperature Humidity Humidity Rainfall\n"
        "==================== =========== =========== ======== ======== ========\n"
    )
    #Filter only unique entries
    uniqueDates = set()
    allLines = []
    #Sort the keys before parsing
    uniqueDates = sorted({entry[:8] for entry in data})
    #Now get each unique entry and get historical data
    for uniqueEntry in uniqueDates:
        #Get the dates
        entryYear = int(uniqueEntry[:4])
        entryMonth = int(uniqueEntry[4:6])
        entryDay = int(uniqueEntry[6:8])
        #Get historical data
        minTemp = min_temperature(data=data,date=uniqueEntry)
        maxTemp = max_temperature(data=data,date=uniqueEntry)
        minHumid = min_humidity(data=data,date=uniqueEntry)
        maxHumid = max_humidity(data=data,date=uniqueEntry)
        totRain = tot_rain(data=data,date=uniqueEntry)
        #Create the date string
        date = f"{calendar.month_name[entryMonth]} {entryDay}, {entryYear}"
        #Create the data string
        line = f"{date:<20} {minTemp:>11} {maxTemp:>11} {minHumid:>8} {maxHumid:>8}    {totRain:>5.2f}\n"
        allLines.append(line)
    return header + "".join(allLines)

#Helper functions ive used before
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