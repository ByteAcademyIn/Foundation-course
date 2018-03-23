"""
Code to prompt the user for hours and rate per hour 
using input to compute gross pay. 

	* Give the employee 1.5 times the hourly rate for hours 
	  worked above 40hrs. 

	* Include try and except to handle non-numeric inputs.

Should use input to read a string and float() to convert 
the string to a number.
"""

#prompts the user to enter no. of hours
hours=input("Please enter the no. of hours : ")

# Handling non-numeric hour value
try : 
	hour_check = float(hours) 

	#prompts the user to enter rate per hour
	rate=input("Please enter your rate per hour : ")

	# Handling non-numeric rate value
	try : 
		rate_check = float(rate) 

		# Computing the gross pay for hours less than or equal to 40hrs
		if hour_check<=40 : 
			pay=hour_check*rate_check

		# Computing the gross pay for hours more than 40hrs
		else :
			pay=(40*rate_check)+((hour_check-40)*rate_check*1.5)

		#Prints the gross pay
		print("Gross pay : ",pay)

	except:
		print("Error! Please enter a numeric value.")

except :
	print("Error! Please enter a numeric value.")
