'''
program to compute pay and overtime pay
Written by Lebohang

'''
#input for hour and rate

hour = float (input ('Enter hours: '))
rate = float (input ('Enter rate: '))

#defining function

def computepay (a,b):

#calculating overtime pay

    if a > 40:
        overtime = (a - 40) * (b * 1.5)
        pay = 40 * b
        total_pay = overtime + pay

#calculating normal pay

    else:
        total_pay = a * b

    return 'total pay', total_pay

#output calling the function

print (computepay (hour, rate))
