# Input from user for number of hours
hours = input("Enter the number of Hours: ")

#Inputfrom user for rate per hour
rate_per_hour = input("Enter the rate per hour: ")

#Calculating gross pay
gross_pay = float(hours) * float(rate_per_hour)

#Printing Gross Pay
print("The gross Pay is " + str(gross_pay) )
