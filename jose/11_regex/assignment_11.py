"""
Finding Numbers in a Haystack. In this assignment you will read through 
and parse a file with text and numbers. You will extract all the numbers 
in the file and compute the sum of the numbers. The numbers can appear 
anywhere in the line. There can be any number of numbers in each line 
(including none).

Desired output:

regex_sum.txt : 445833
regex_sum_1.txt : 466318

"""

# importing regex
import re

# prompts the file name
f_name=input("Please enter the file name: ")

#checks file name 
try:
	f_hand=open(f_name)
except:
	print("Error!",f_name,"not found.")
	quit()

#filtering using regex
numlist=list()
for line in f_hand:
	line=line.rstrip()
	stuff=re.findall("([0-9]+)",line)
	
	#appends to numlist
	for x in range(len(stuff)):
		num=float(stuff[x])
		numlist.append(num)

#prints output
print(f_name,sum(numlist))
