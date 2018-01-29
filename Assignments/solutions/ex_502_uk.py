"""

 This is a program that repeatedly prompts a user for integer numbers until the user enters
'done'. Once 'done' is entered, print out the largest and smallest of the numbers.
If the user enters anything other than a valid number catch it with a try/except and put out
an appropriate message and ignore the number.
 """

#printing the initial instructions

print ( "  Instructions Kindly Enter Number one by one " )
print( " Please enter the word /done/ to find the max and min numbers \n ")

#assigning the variables initial value

small = None
large= None
num=list()
#looping to compute the total and count

while True :
    n = raw_input( " please enter the number  :  " )
    if n == 'done' : break

#try and except to ensure only accepted values

    try :
        x = float(n)

    except :
        print("enter a correct input")
        continue
    num.append(n)
    if(small==None):
        small=n
    if n < small :
        small = n
    elif n >large :
        large = n

#printing the final output
print ( " \n The largest number is : " , large ,  '\n' )
print ( " \n the smallest number is : ", small , " \n " )
print ( " \n total list of numbers inputted is : " , num , " \n " )
print ( " \n ThankYou for using our services \n " )
