""" Code to check if the first number is divisible by the second number or if 
	the second number is divisible by the first number or if neither are divisible 
	with each other.
"""

# User enters the numbers

number_1 = int(input("Enter the first number:"))
number_2 = int(input("Enter the second number:"))

# Computes if the first number is divisible by the second number

if (number_1%number_2) == 0 :
	print("First number is divisible by the second number.")

# Computes if the second number is divisible by the first number

elif (number_2%number_1) == 0 :
	print("Second number is divisible by the first number.")

# Computes if neither are divisible with each other

else: 
	print("It's not divisible.")
	