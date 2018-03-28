"""
Print the pattern:
*
**
***
****
n = number of lines (provided by the user)
"""

#Prompts to enter the no. of lines
n=int(input("Please enter the no. of stars in the base: "))

#python way
for i in range(1,n+1):
	print("* "*i)

#c way
# for i in range(1,n+1):
# 	for j in range(1,i+1):
# 		print("*",end="")
# 	print("")

# for i in range(1,n+1):
# 	for j in range(1,i+1):
# 		for k in range(1,(n+1)-j):
# 			print(" ",end="")
# 		print("*",end="")
# 	print("")

#    *
#   * *
#  * * *
# * * * *