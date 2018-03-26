"""
Code to find the factorial of a number 
"""

#Prompt the number
num=int(input("Please enter a number: "))

# Using while loop
i=1
fact=1  
while i<= num:
	fact=i*fact
	i=i+1
print(num,"!=",fact)

# Using for loop
# fact=1
# for i in range(1,num+1):
# 	fact=fact*i
# print(num,"!=",fact)	


