#a program to find the factorial of a user inputted number

#input prompt
x = int(input('Enter a number: '))

#initializing variable 'sum' and i
fact = 1
i = 1
#loop to multiply the numbers
while i <= x :
    fact = fact * i
    i = i + 1
#output the number
print(fact)
