'''
Write a program that repeatedly prompts a user for integer numbers until the
user enters 'done'. Once 'done' is entered, print out the largest and smallest
of the numbers. If the user enters anything other than a valid number catch it
with a try/except and put out an appropriate message and ignore the number.
'''

#initializing iteration variable
i = None

#initializing variables for largest and smallest numbers
largest = None
smallest = None

#while loop runs until user enters done
while i != 'done':

    #input prompt
    i = input('Enter a number: ')

    try:
        #check if data is numeric
        x = int(i)
    except:
        #check if user has entered 'done'
        if i != 'done':
            
            #print error message and run loop again for invalid data
            print('Error: Invalid input')
            continue

    #check if number is the largest so far
    if largest is None:
        largest = x
    elif x > largest:
        largest = x

    #check if number is the smallest so far
    if smallest is None:
        smallest = x
    elif x < smallest:
        smallest = x

#printing the largest and smallest numbers
print('The largest number was ', largest)
print('The smallest number was ', smallest)
