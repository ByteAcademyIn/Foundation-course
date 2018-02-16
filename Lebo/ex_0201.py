'''

A program to compute to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
pay program using try and except so that your program handles non-numeric input

'''

#Compiled by Lebohang Mashatola

#Input the number of hours and rate per hour

try:
    hour = float (input ('Enter number of hours: '))
    rate = float (input ('Enter rate per hour: '))

#Computing overtime pay

    if hour > 40:
        overtime = (hour - 40) * (rate * 1.5)
        pay = 40 * rate
        total_pay = overtime + pay
        print ('Total revised pay:', total_pay)

#Computing normal hours pay

    else:
        total_pay = rate * hour
        print ('Total pay:', total_pay)

#Saving grace

except:
    print ('ERROR, use numericals')
