"""
Code that repeatedly prompts a user for integer numbers until the 
user enters 'done'. Once 'done' is entered, print out the largest 
and smallest of the numbers. If the user enters anything other than 
a valid number catch it with a try/except and put out an appropriate
message and ignore the number.

"""

#initialising largest and smallest with None
largest=None
smallest=None

while True:

	#Prompts the user to enter a number or type done:
	inp=(input('Please enter a number or type "done": '))

	#detects "done" breaks the loop
	if inp=="done":
		break
	try:

		#Filters non-numeric values
		num=float(inp)
	except:

		#Prints the error and continues back to loop
		print("Invalid input.")
		continue

	#computes largest and smallest numbers
	if largest is None:
		largest=num
	elif num>largest:
		largest=num
	if smallest is None:
		smallest=num
	elif num<smallest:
		smallest=num

#prints the result
print("Largest number:",largest," Smallest number:",smallest)
