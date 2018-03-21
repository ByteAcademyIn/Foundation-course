"""
Question:
Write a program to prompt the user for hours and rate per hour using input to
compute gross pay. Use 35 hours and a rate of 2.75 per hour to test the program
(the pay should be 96.25). You should use input to read a string and float() to
convert the string to a number. Do not worry about error checking or bad user
data.
"""

# Input prompt for the number of hours and rate
hours = input('Enter number of hours ')
rate = input('Enter rate per hour ')
# Calculation of gross pay
pay = (float(hours)) * (float(rate))
# Output
print('gross pay= ', pay)
