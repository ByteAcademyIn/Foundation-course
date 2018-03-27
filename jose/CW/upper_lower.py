"""
Code to count the upper and lower characters in a word
"""


#Prompts the word
wrd=input("Please enter the word: ")

#initialising upper and lower with 0
upper=0
lower=0

#using the islower and isupper fuctions
for x in wrd:
	if x.islower():
		lower+=1
	elif x.isupper():
		upper+=1

#prints the word
print("Upper characters:",upper,"Lower characters:",lower)

