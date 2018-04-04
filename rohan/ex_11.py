'''
Finding Numbers in a Haystack In this assignment you will read through and
parse a file with text and numbers. You will extract all the numbers in the
file and compute the sum of the numbers. The numbers can appear anywhere in the
line. There can be any number of numbers in each line (including none).

Desired output:

regex_sum.txt : 445833
regex_sum_1.txt : 466318
'''
#importing the regex library
import re


#input prompts
filename = input('Enter file path: ')
if filename == '': filename = '/Users/rohandatar/Foundation-course/Assignments/11_regex/regex_sum.txt'

#opening the file
file = open(filename)

#reading the file
text = file.read()

#finding the Numbers
num = re.findall('[0-9]+', text)

#converting the numbers from string type
for i in range(len(num)):
    num[i] = int(num[i])

#printing the sum of the numbers
print('sum:',sum(num))
