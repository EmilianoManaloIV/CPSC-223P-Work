#Create a list
#Create the function that adds an element to the array string
def my_insert(myList, index, value):
    #Cut the string into pieces using slicing
    left_half = myList[:index]
    right_half = myList[index:]
    #print(left_half)
    #print(right_half)
    left_half.append(value)
    left_half.extend(right_half)
    return left_half
list = ['p','y','t','h','n']
print(my_insert(list,4, 'o'))
