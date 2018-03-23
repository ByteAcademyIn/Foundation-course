# Get a number from the user and check if it is an integer or not

#input prompt
x= input('enter an integer: ')

#string check
try:
	y= float(x)
except:
	print('not an integer')


#print(y)

#float check
#z= y/0.1
if (y%1)!=0:
	print('not an integer')
else:
	print('it is an integer')
