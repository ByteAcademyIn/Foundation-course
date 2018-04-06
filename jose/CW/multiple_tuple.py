"""
Code to prompt for inputs and output as a list of tuples
"""

tup=[]

#while
while True:
	#input
	inp=input("Enter the values:")
	if inp == "":
		break

	tup.append(tuple(inp.split(",")))
print(tup)






