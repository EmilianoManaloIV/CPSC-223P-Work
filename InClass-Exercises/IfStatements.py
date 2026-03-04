x = int(input("PLeaser enter the integer: "))
#Now decide what to do with this "x" data
if x < 0:
	x = 0
	print("Negative changed to zero")
elif x == 0:
	print("zero")
elif x == 1:
	print("single")
else:
	print('More')