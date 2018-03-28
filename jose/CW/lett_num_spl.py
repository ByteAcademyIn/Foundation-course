"""
Code to count the letters numbers and spl. characters
"""

#Prompts the word
data=input("Please enter the data: ")

#initialising upper and lower with 0
lett=0
num=0
spl=0

#using the islower and isupper fuctions
for x in data:
	if (x>="a" and x <="z") or (x>="A" and x <= "Z"):
		lett+=1
	elif (x>="0" and x<="9"):
		num+=1
	else:
		spl+=1

#prints the word
print("Letters:",lett,",Numbers:",num,",Special characters:",spl)

