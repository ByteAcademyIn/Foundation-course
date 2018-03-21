"""
A program to prompt the user for hours and rate per hour 
using input to compute gross pay. Use 35 hours and 
a rate of 2.75 per hour to test the program (the pay should be 96.25). 
Should use input to read a string and float() to convert the string to a number.
"""

#prompts the user to enter no. of hours
hours=input("Please enter the no. of hours: ")

#prompts the user to enter rate per hour
rate=input("Please enter your rate per hour: ")

#Computing the gross pay
pay=float(hours)*float(rate)

#Prints the gross pay
print("Gross pay is: ",pay)
