from weather import *

#Default file name
defaultFileName = "defaultData"

#Weather dictionary
weatherDict = {}

currentInput = -1
while currentInput != 9:
    #Prompt user for input and verify that its allowed
    print("*** TUFFY TITAN WEATHER LOGGER MAIN MENU")
    print("1. Set data filename")
    print("2. Add weather data")
    print("3. Print daily report")
    print("4. Print historical report")
    print("9. Exit the program")
    currentInput = int(check_if_input_null_or_not_digit(input("Enter Menu Choice: ")))
    #Go through the core logic
    if currentInput == 1:
        weatherDict = weather(fileName = input("Enter data filename: "))
    elif currentInput == 2:
        date = input("Enter Date (YYYYMMDD): ")
        time = input("Enter Time (hhmmss): ")
        temp = input("Enter Temperature: ")
        humid = input("Enter Humidity: ")
        rain = input("Enter Rainfall: ")
        weatherDict[f"{date}{time}"]={"t":temp,"h":humid,"r":rain}
        write_data(data=weatherDict,fileName=defaultFileName)
    elif currentInput == 3:
        print(report_daily(data = weatherDict, date = input("Enter Date (YYYYMMDD): ")))
    elif currentInput == 4:
        print(report_historical(data=weatherDict))
    else:
        print("Invalid Input! Try Again!")
