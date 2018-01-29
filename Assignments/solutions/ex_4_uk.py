""" This is a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Award time-and-a-half for the hourly rate for all hours worked above 40 hours. A function is defined
to do the computation of time-and-a-half in a function called computepay()
Check Criteria : Use 45 hours and a rate of 10.50 per hour to test
the program (the pay should be 498.75). You should use input to read a string and float() to convert
the string to a number."""

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
     #defining function to compute overtime pay.
def computepay():
        pay = hr * rate
        pay = pay + (hr-40) *  (rate * 1.5)

# pay calculation for more than 40 hours ( hours x rate )
if hr>40:
    pay = computepay()
#pay calculation for <= 40 hours
else :
    pay = hr * rate
print ("The amount earned is",pay, "USD for a period of" ,hr, "hours @ rate" , rate)
exit()
