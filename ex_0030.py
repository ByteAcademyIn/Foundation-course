#Input from user for number of hours and rate per hour
hours = float(input("Enter the number of hours worked: "))
rate_per_hour = float(input("Enter the wage rate per hour: "))

#Calculating additional number of hours worked( above 40)
b = hours - 40

#Calculating and printing grosspay
if(b>0):
  print("Gross Pay is = " + str((40*rate_per_hour)+(b*1.5*rate_per_hour)))

else:
  print("Gross Pay is = " + str(hours*rate_per_hour))
