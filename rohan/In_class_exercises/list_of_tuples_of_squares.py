'''
get a number from the user and output a list of numbers and their squares in the
form of a list of tuples
'''

#input prompts
num = int(input('Enter a number: '))

lst = []

d = {}

l = []
for i in range(1, (num+1)):
    j= i**2
    lst.append((i,j))
    d[i]=j
    l.append(j)
print(lst)
print(d)
print(l)
