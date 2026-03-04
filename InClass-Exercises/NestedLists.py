#Make a dictionary
employees ={
    1:{"name":"Joe Klein", 'job':'manager'},
    2:{"name":"Mary Pham", 'job':"developer"},
    3:{"name":"Jim Gomez", 'job':'developer'}
}

mylist=[]
for x, y in employees.items():
    mylist.append(y['job'])

print(mylist)