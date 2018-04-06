"""
Write a program that prompts for a file name, then opens that file 
and reads through the file, looking for lines of the form:

X-DSPAM-Confidence: 0.8475

Count these lines and extract the floating point values from each 
of the lines and compute the average of those values and produce 
an output as shown below. Do not use the sum() function or 
a variable named sum in your solution.

Enter 'mbox-short.txt' as the file name.

Desired Output:
Average spam confidence: 0.750718518519
"""

#prompts for a file name
f_name=input("Please enter the file name: ")

#checks file name 
try:
	f_hand=open(f_name)
except:
	print("Error!",f_name,"not found.")
	quit()

#initialising count and tot
count=0
tot=0

#counts, extracts and adds the floating point values
for line in f_hand:
	if "X-DSPAM-Confidence" in line:
		count+=1
		f_pos=line.find(":")
		num=float(line[f_pos+1:])
		tot+=num

#prints the average
print("Average SPAM confidence:",tot/count)

