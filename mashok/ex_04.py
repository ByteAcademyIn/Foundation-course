""" use def function to compute wage cost and call the function to perform
specific calculation """
def computepay(hours, rate_float)
    if (hours < 40) :
        Wage_cost = hours * rate_float
        return Wage_cost
    else:
        Wage_cost_bonus = hours * 1.5 * rate_float
        return Wage_cost_bonus
hours = int(input("Enter number of hours worked: "))
rate = input("Enter hourly wage rate: ")
rate_float = float(rate)
print(computepay())
