

""" Write a program that prompts for a file name, then opens that file and reads through the file,
looking for lines of the form:

X-DSPAM-Confidence: 0.8475

Count these lines and extract the floating point values from each of the lines and compute
the average of those values and produce an output as shown below. Do not use the sum() function
or a variable named sum in your solution.

Enter 'mbox-short.txt' as the file name. """

filename = raw_input ( " Enter the file name Please : ")
fhandle = open(filename,'r')

count=0
total=0
for line in fhandle:
    line=str(line)
    if line.startswith('X-DSPAM-Confidence:') :
        pos=line.find('0')
        temp=float(line[pos:])
        count=count+1
        total=total+temp
        continue
print ( " the total numbers of mentioned type found were " , count )
print ( " the average of those numbers is " , (total/count) )
