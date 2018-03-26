"""
Write a program that repeatedly prompts a user for integer numbers 
until the user enters 'done'. Once 'done' is entered, print out the 
largest and smallest of the numbers. If the user enters anything 
other than a valid number catch it with a try/except and put out 
an appropriate message and ignore the number.
"""

#initialising large and small
largest=None
smallest=None

while True:
	#Prompts the user to enter a number or type done:
	n=(input('Please enter a number or type "done": '))
	#detects "done" breaks the loop
	if n=="done":
		break
	try:
		#Filters non-numeric values
		large=float(n)
		small=float(n)
	except:
		#Prints the error
		print("Invalid input.")
		#continues back to loop
		continue

	#computes largest and smallest numbers
	if largest is None:
		largest=large
	elif large>largest:
		largest=large
	if smallest is None:
		smallest=small
	elif small<smallest:
		smallest=small

#prints the result
print("Largest number:",largest," Smallest number:",smallest)
