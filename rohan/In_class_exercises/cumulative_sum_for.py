#a program to find the sum of the numbers to a user inputted number

#input prompt
x = int(input('Enter a number: '))

#initializing variable 'sum'
sum = 0

#loop to add the numbers
for i in range(x+1):
    sum = sum + i

#output the number
print(sum)
