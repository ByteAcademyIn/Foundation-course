"""Write a program which repeatedly reads numbers until 
the user enters "done". Once "done" is entered, print out 
the total, count, and average of the numbers. If the user 
enters anything other than a number, detect their mistake 
using try and except and print an error message and skip 
to the next number."""

#initialising total, count and average
tot=0
cnt=0
avg=0

while True:
	#Prompts the user to enter a number or type done:
	n=(input('Please enter a number or type "done": '))
	#detects "done" breaks the loop
	if n=="done":
		break
	try:
		#Filters non-numeric values
		num=float(n)
	except:
		#Prints the error
		print("Invalid input.")
		#continues back to loop
		continue

	#computes total, count and average
	tot=tot+num
	cnt=cnt+1
	avg=tot/cnt
#prints the result
print("Total:",tot," Count:",cnt," Average:",avg)
