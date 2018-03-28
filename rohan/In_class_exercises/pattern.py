'''
Print the pattern:
*
**
***
****
n = number of lines (provided by the user)
'''

#input prompt
n = int(input('Enter the number of lines: '))

#iterating to n for the pattern
for i in range(1, (n+1)):

    #printing the pattern
    print('*'*i)
