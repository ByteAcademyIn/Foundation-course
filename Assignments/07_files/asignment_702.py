

""" Write a program that prompts for a file name, then opens that file and reads through the file,
looking for lines of the form:

X-DSPAM-Confidence: 0.8475

Count these lines and extract the floating point values from each of the lines and compute
the average of those values and produce an output as shown below. Do not use the sum() function
or a variable named sum in your solution.

Enter 'mbox-short.txt' as the file name. """

#opening File by taking input from user
filename = raw_input ( " Enter the file name Please : ")
fhandle = open(filename,'r')
#assigning the initial values to dummy variables
count=0
total=0

#iterating through each line to find the match and using dummy variables to count and add
for line in fhandle:
    line=str(line)
    if line.startswith('X-DSPAM-Confidence:') :
        pos=line.find('0')
        temp=float(line[pos:])
        count=count+1
        total=total+temp
        continue
# output print
print ( " the total numbers of mentioned type found were " , count )
print ( " the average of those numbers is " , (total/count) )
