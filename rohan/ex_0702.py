'''
Write a program that prompts for a file name, then opens that file and reads
through the file, looking for lines of the form:

X-DSPAM-Confidence: 0.8475

Count these lines and extract the floating point values from each of the
lines and compute the average of those values and produce an output as shown
below. Do not use the sum() function or a variable named sum in your solution.

Enter 'mbox-short.txt' as the file name.

Desired Output:
Average spam confidence: 0.750718518519
'''

#defining function to extract the number from a line of text
def num(line):

    #Finding the number
    x = line.find(':')

    #extracting the number
    n = line[x+1:]

    #returning the number
    return float(n)

#input prompt
filename = input('Enter a file path: ')

#initializing total and counter variables
total = 0
count = 0

#opening the file
file = open(filename)

for line in file:
    if 'X-DSPAM-Confidence:' in line:
        total = total + num(line)
        count +=1

#printing the Average
print('Average spam confidence: ', (total/count) )
