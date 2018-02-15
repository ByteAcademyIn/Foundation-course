'''
input the number from user and to find the number as integer or decimal
'''
num= input('please enter a number')
float(num)
if (float(num)== int(num)):
    print(num, 'is integer')
else:
    print(num, 'is float')
