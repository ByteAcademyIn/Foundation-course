'''
write a program to get two numbers and an operator from the user and perform
the operation
'''

#addition function
def add(a,b):
    x = a + b
    return x
#subtraction function
def subtract(a,b):
    x = a - b
    return x
#multiplication function
def multiply(a,b):
    x = a * b
    return x
#division function
def divide(a,b):
    x = a/b
    return x

#input prompts
a = float(input('Enter a number: '))
b = float(input('Enter a number: '))
c = input('Enter an operator: ')

if c == '+':
    print(add(a,b))
elif c == '-':
    print(subtract(a,b))
elif c == '*':
    print(multiply(a,b))
elif c == '/':
    print(divide(a,b))
