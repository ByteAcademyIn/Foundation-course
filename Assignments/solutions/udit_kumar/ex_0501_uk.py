""" This is a program which repeatedly reads numbers until the user enters
"done". Once "done" is entered, the total, count, and average of the numbers is printed.
If the user enters anything other than a number, their mistake is detected using try and except
and an error message is printed to skip to the next number.
Example:
Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.333333333333333 """

#printing the initial instructions

print ("Kindly Enter Number one by one for which calculation is requried \n.")
print("Please enter the word \done\ to calculate the total , count and average of numbers \n")

#assigning the variables initial value

num = 0
totl= 0

#looping to compute the total and count

while True :
    n = raw_input("please enter the number  :  ")
    if n == 'done' : break

#try and except to ensure only accepted values

    try :
        x = float(n)

    except :
        print("Enter a correct input")
        continue

    num = num + 1
    totl = totl + x

#printing the final output
print ("\n The Total is : " , totl , "\n" )
print ("\n the Average is : ", totl/num , "\n" )
print ("\n total count of numbers inputted is : " , num , "\n" )
print ("\n ThankYou for using our services \n" )
