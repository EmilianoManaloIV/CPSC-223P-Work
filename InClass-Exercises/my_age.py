#Cacluate the age based on a given input
import sys
def print_age(birthYear):
    currentYear = 2026
    print("You are " + str(currentYear - birthYear) + " years old")
if(__name__ == "__main__"):
    print_age(int(sys.argv[1]))