#Given list of words
word = ["hello", "abba", 'cc', "wow", ]
#Set the element counter
LISTELEMENTS = 0
#For every element, see if their wor
for w in word:
    #Check if the beginning and the end are the same, then check length
    if w[0] == w[-1] and len(w) > 1:
        #Increment the counter by one
        LISTELEMENTS+=1
print("Amount of elements in the list that have the same character in the beginning and the end: ", LISTELEMENTS)