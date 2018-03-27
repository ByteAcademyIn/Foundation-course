'''
find the number of characters in a string without using the len() function
'''

#define the function
def counter(string):
    #initializing the counter
    count = 0
    #iterating over the string
    for i in string:
        count = count + 1
    return count

#input prompt
string = input('Enter a string ')
#output
print(counter(string))
