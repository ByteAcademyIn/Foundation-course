""" This is a program to prompt the user for hours and
rate per hour using input to compute gross pay.
Use 35 hours and a rate of 2.75 per hour to test the program
(the pay should be 96.25). You should use input to read a string and float()
 to convert the string to a number. Do not worry about error checking or bad
 user data."""

 # Hour input
print ("Please enter the hours worked this week")
hr = input ()
try:
     hr = float(hr)
except:
     hr = 0
     print ("Error: number of hours not entered correctly")

# Rate Input
print ("Please enter the unit rate (USD/Hr) as per your employement contract")
rate = input ()
try:
     rate = float(rate)
except:
     rate = 0
     print ("Error: Rate not entered correctly")

# pay calculation ( hours x rate )
pay = hr * rate
print ("The amount earned is", pay , "USD for a period of" ,hr, "hours @ rate" , rate)
