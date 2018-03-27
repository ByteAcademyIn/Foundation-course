'''
enter a string and count the number of uppercase and lowercase letters
'''

#input prompt
string = input('enter a word ')

#initializing counters for uppercase and lowercase
lcount = 0
ucount = 0

#iterating over a string
for i in string:
    if (i >= 'A') and (i <= 'Z'):
        ucount += 1
    elif (i >= 'a') and (i <= 'z'):
        lcount += 1

print('number of uppercase letters = ', ucount)
print('number of lowercase letters = ', lcount)
