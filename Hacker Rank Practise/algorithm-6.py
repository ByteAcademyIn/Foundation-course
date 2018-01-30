# to find the fraction of 0 , + and -ve in the list of numbers

# Asking user for limit
num=int(input ( " Please Enter the count of Numbers You will Input : " ))

# inputting the list of numbers
num_list=[int(i) for i in input('Please Enter the Numbers separated by space ').split()]

#Creating a new list with + - 0 count

dummy=['p' for i in num_list if i>0]
dummy+=['n' for i in num_list if i<0]
dummy+=['zero' for i in num_list if i ==0 ]

# printing the results
print( " the fraction of negatives in the entered list is " , (dummy.count('n')/num) )
print( " the fraction of positives in the entered list is " , (dummy.count('p')/num) )
print( " the fraction of zeros in the entered list is " , (dummy.count('zero')/num) )
