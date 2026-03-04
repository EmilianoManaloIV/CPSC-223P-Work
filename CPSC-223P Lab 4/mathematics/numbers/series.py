#Sums all values within a given list
import builtins
def sum(*, list):
    return builtins.sum(list)
#Averages the values in the list
def average(*, list):
    return builtins.sum(list)/len(list)
