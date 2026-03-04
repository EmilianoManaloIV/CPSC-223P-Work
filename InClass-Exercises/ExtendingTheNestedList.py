#Base list
list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
#Additional List
sub_list =  ['h','i','j']
#Adds the list and reassigns
list1[2][1][2] += sub_list
#Prints out the list
print(list1)
