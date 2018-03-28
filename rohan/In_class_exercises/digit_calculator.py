'''
get a digit from the user as a and calculate a+aa+aaa+aaaa
'''

a = input('Enter a digit: ')

total =0

for i in range(1,5):
    x= a*i
    y= int(x)
    total = total + y

print(total)
