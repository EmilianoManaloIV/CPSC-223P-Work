#Create a dictionary
tel={'Jack':4098, "Sape":4139}
#Print the dictionary
print(tel)
#Add a new element to the list
tel["Guido"]=4127
#Print it again!
print(tel)
#Delete an element off the list
#del tel['Jack']
#Print once more!
print(tel)
#Cast the dictionary!
x = list(tel)
#Print it again!
print(x)
#Print just the keys!
for element in tel:
    print(element,tel[element])
#Another method! Using a dictionary method!
for x, y in tel.items():
    print(x,y)

