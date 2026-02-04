#How to reverse a list manually in python
#Create a list
myList = [1,2,3,4,5,6]
#At least run half the length of the list
for i in range(int(len(myList)/2)):
    #Save the current element
    temp=myList[i]
    #Swap the value over to the right
    myList[i]=myList[len(myList)-1-i]
    #Replace back the move temp
    myList[len(myList)-1-i]-temp
#Print the list
print(myList)
#Try to write on paper to solve problems if possible
