#a program to find the sum of the numbers to a user inputted number

#input prompt
x = int(input('Enter a number: '))

#initializing variable 'sum' and i
sum = 0
i = 0
#loop to add the numbers
while i <= x :
    sum = sum + i
    i = i + 1
#output the number
print(sum)
