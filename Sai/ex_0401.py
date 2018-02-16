"""
Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Award time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of time-and-a-half in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function
"""

#Input from user for number of hours and rate per hours
hours = float(input("Enter the number of hours: "))
rate_per_hour = float(input("Enter the wage rate per hour: "))

#Defining the function Computepay()
def computepay(hours,rate_per_hour):
	if(hours >0):
		gross_pay = (hours*rate_per_hour) + ((hours-40)*0.5*rate_per_hour)
	else:
		gross_pay = (hours*rate_per_hour)
	return gross_pay
	
print computepay(hours,rate_per_hour)
