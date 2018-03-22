"""
Code to implement fizz buzz 
"""


#prompts to enter a number
num=int(input("Enter a number: "))


#defining the function
def fizzbuzz(val):

	if ((val % 3)==0 and (val % 5) == 0) :
		return "fizz_buzz"
	elif (val % 3)==0:
		return "fizz"
	elif (val % 5)==0:
		return "buzz"
	

#calling the function
print(fizzbuzz(num))

