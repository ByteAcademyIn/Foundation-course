# Code to check if the value entered is an integer or not.

# User enters the number

user_value = input("Please enter the number: ")

# filters strings from intergers and floats

try : 
	int_test = int(user_value)

	# filters integers from floats and prints integer or not

	if (type(int_test) == int) : 
		print("Yes! The value entered is an integer.")

except : 
	print("Nope, the value entered is not an integer.")