#program to compute the gross pay based on the rate per hour and hours spent at work
#written by Lebohang Mashatola

#input for the amount of hours spent at work and the rate per hour

hours = input ('Enter the amount of hours spent at work: ')
rate = input ('Enter the rate per hour: ')

#calculation for the total pay

pay = float(hours) * float (rate)

#output

print ('Your total pay is:', pay)
