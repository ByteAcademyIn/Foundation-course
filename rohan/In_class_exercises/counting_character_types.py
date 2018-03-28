'''
program to count the number of letters, numbers and special characters in a
string
'''

#input prompt
string = input('Enter a string: ')

#initializing counter variables
count_letters = 0
count_numbers = 0
count_spchar = 0

#iterating over the string
for char in string:

    #checking for letters
    if ((char >= 'A') and (char <= 'Z')) or ((char >= 'a') and (char <= 'z')):
        count_letters += 1

    #checking for numbers
    elif (char >= '0') and (char <= '9'):
        count_numbers += 1

    #special characters
    else:
        count_spchar += 1

print(count_spchar, count_letters, count_numbers)
