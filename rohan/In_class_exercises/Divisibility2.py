'''
program to find all the numbers between 2000 and 3200 that are divisible by 7
but are not multiples of 5
'''

#Loop of numbers from 2000 to 3200
for i in range(2000, 3201):
    if ((i % 7) == 0) and ((i % 5) != 0 ):
        print(i)
