#For range of numbers from 2,3,4,etc.
for num in range(2,10):
	#Check if divisible by two
	if num % 2 == 0:
		#Print if found even numbers
		print("Found an even number", num)
		continue
	#Found an odd number
	print("Found an odd number", num)