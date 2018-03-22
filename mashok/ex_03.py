""" Write a prgram to compute wages. Upto 40 hours the wages are 10
and above 40 hours the employee is eligible for 1.5 times the normal wages"""

# User inputs
hours = input("Enter number of hours worked: ")
hourly_rate = input("Enter hourly wage rate: ")
# Check to validate data type for No_of_hours
try :
     n_hours = int(hours)
# Check to validate data type for hourly wage rate
except :
    print("Give me a number for hours worked, please")
try :
        f_hourly_rate = float(hourly_rate)
except :
    print("Give me a number for hourly wage rate, please")
if n_hours > 40 :
# Formula
    Wage_cost = (n_hours * f_hourly_rate) + (n_hours - 40) * 0.5 * f_hourly_rate
else :
# Formula
        Wage_cost = (n_hours * f_hourly_rate)
print('wage cost is', Wage_cost)
