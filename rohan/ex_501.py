'''
Write a program which repeatedly reads numbers until the user enters "done".
Once "done" is entered, print out the total, count, and average of the numbers.
If the user enters anything other than a number, detect their mistake using try
and except and print an error message and skip to the next number.

Example:

Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.333333333333333
'''

#Initializing iteration variable
i = None

#Initializing total and count variables
total = 0
count = 0

#Loop user enters done
while i != 'done':
    i = input('Enter a number: ')

    #try to convert data to numeric format
    try:
        x = float(i)
    except:

        #check if data is invalid or if user is trying to exit the loop
        if i == 'done':
            #exit the loop if user enters 'done'
            break
        else:
            #start the loop again for invalid data
            print('Invalid input')
            continue

    #incrementing count and adding to total
    total = total + x
    count = count + 1

#printing the total count and average (total/count)
print(total, count, (total/count))
