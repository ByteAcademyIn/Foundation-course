""" This is a program to prompt the user for hours and rate per hour
using input to compute gross pay. Pay the hourly rate for the hours up
to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
Use 45 hours and a rate of 10.50 per hour to test the program (the pay
should be 498.75). You should use input to read a string and float() to
convert the string to a number. Do not worry about error checking the user
 input - assume the user types numbers properly.
"""

 # Hour input
print ("Please enter the hours worked this week")
hr = input ()
try:
     hr = float(hr)
except:
     hr = 0
     print ("Error: number of hours not entered correctly")
     exit()

# Rate Input
print ("Please enter the unit rate (USD/Hr) as per your employement contract")
rate = input ()
try:
     rate = float(rate)
except:
     rate = 0
     print ("Error: Rate not entered correctly")
     exit()

# pay calculation for more than 40 hours ( hours x rate )
if hr>40:
    pay = hr * rate
    pay = pay + (hr-40) *  (rate * 1.5)
#pay calculation for <= 40 hours
else :
    pay = hr * rate
print ("The amount earned is", pay , "USD for a period of" ,hr, "hours @ rate" , rate)
exit()
