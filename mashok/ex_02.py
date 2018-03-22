""" Write a prgram to compute wages. Upto 40 hours the wages are 10
and above 40 hours the employee is eligible for 1.5 times the normal wages"""

# User inputs
No_of_hours = input("Enter number of hours worked: ")
Hourly_rate = input("Enter hourly wage rate: ")
Hourly_rate_float = float(Hourly_rate)

# Check whether number of hours worked is greater than 40
if Num_No_of_hours > 40 :
# Calculate wage cost
    Wage_cost = (Num_No_of_hours * Hourly_rate_float) + (Num_No_of_hours - 40) * 0.5 * Hourly_rate_float
else :
# Calculate wage cost
    Wage_cost = (Num_No_of_hours * Hourly_rate_float)
print('wage cost is', Wage_cost)
