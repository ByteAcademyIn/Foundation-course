"""
Code to prompt the user for hours and rate per hour 
using input to compute gross pay. 

	* Give the employee 1.5 times the hourly rate for 
	  hours worked above 40hrs. 

Should use input to read a string and float() to convert 
the string to a number.
"""

# Prompts the user to enter no. of hours
hours=input("Please enter the no. of hours : ")

# Prompts the user to enter rate per hour
rate=input("Please enter your rate per hour : ")

# Computing the gross pay for hours less than or equal to 40hrs
if float(hours)<=40 : 
	pay=float(hours)*float(rate)

# Computing the gross pay for hours more than 40hrs
else :
	pay=(40*float(rate))+((float(hours)-40)*float(rate)*1.5)

#Prints the gross pay
print("Gross pay : ",pay)
