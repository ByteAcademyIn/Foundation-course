'''
store the squares of the numbers upto a user entered number in a list
'''

#num = int(input('Enter a number: '))
num=20
squares = list()
for i in range(num + 1):
    squares.append(i**2)

print(squares[:(len(squares)-5)])
#print(len(squares))
