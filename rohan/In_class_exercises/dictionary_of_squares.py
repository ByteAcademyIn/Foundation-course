'''
take a user entered number and create a dictionary with the squares of the
numbers upto the number as values and the numbers as keys
'''

#input prompt
#num = int(input('Enter a number: '))
num=5
#initializing dictionary
squares = dict()
even_limit=int(input('enter a number: '))


for i in range(1,(num+1)):
    squares[i] = i**2

for j in range(2,(even_limit+1),2):
    #x=str(j)
    squares[j]=squares.get(j,j**2)

print(squares)
