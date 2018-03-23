"""
Code to prompt the user for hours and rate per hour using input
to compute gross pay. Award time-and-a-half for the hourly rate for all hours
worked above 40 hours. Put the logic to do the computation of time-and-a-half
in a function called computepay() and use the function to do the computation.
The function should return a value. Use 45 hours and a rate of 10.50 per hour
to test the program (the pay should be 498.75). You should use input to read a
string and float() to convert the string to a number. Do not worry about error
checking the user input unless you want to - you can assume the user types
numbers properly. Do not name your variable sum or use the sum() function.

"""
# Defining function to compute the gross pay for hours more than 40hrs
def computepay(h,r):
	payment=(40*r)+((h-40)*r*1.5)
	return payment

# Prompts the user to enter no. of hours
hours=input("Please enter the no. of hours : ")

# Handling non-numeric hour value
try:
	hour_check = float(hours)

	# Prompts the user to enter rate per hour
	rate = input("Please enter your rate per hour : ")

	# Handling non-numeric rate value
	try:
		rate_check = float(rate)

		# Computing the gross pay for hours less than or equal to 40hrs
		if hour_check <= 40:
			pay = hour_check*rate_check

		# Calling function to compute the gross pay for hours more than 40hrs
		else:
			pay = computepay(hour_check,rate_check)

		# Prints the gross pay
		print("Gross pay : ",pay)

	except:
		print("Error! Please enter a numeric value.")

except:
	print("Error! Please enter a numeric value.")