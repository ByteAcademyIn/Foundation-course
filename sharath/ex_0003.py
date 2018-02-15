#This is a python program to calculate gross pay

Hours = input('Enter number of working hours : ') #Working hours
Rate = input('Enter rate charged per hour : ') #Rate charged

#Code to check if the user has typed in a character

try:
    iHours = int(Hours)
    iRate = int(Rate)
except:
     iHours = -1
     iRate = -1

if iHours > 0:
    print('Nice Work')
elif iRate >0:
    print('Nice Work')
else:
    print('Error Please enter a numeric input')

#Converting the input into float
WorkingHours = float(Hours)
RateperHour = float(Rate)

#Pay = WorkingHours * RateperHour
#(Uncomment to calclate the pay)

# Calucating the Overtime if the user has worked over time (above 40 hours) and increasing Overtime pay by 1.5
if WorkingHours <= 40:
    print  (WorkingHours * RateperHour)
else:
    print ((WorkingHours * RateperHour)+(WorkingHours-40)*RateperHour*1.5)
