#This is a python program to calculate gross pay

Hours = input('Enter number of working hours : ') #Working hours
Rate = input('Enter rate charged per hour : ') #Rate charged

#Converting the input into interger
WorkingHours = int(Hours)
RateperHour = int(Rate)

#Multiplying
Pay = WorkingHours * RateperHour

#print Pay
print("Your pay for the day is RS ", Pay)
