""" a program to extract numbers from a txt file where numbers appear
 randomly"""

import re
# lines to open and read the text file
file = input("enter a file name: ")
fhandle =  open(file)

# creating a empty list to which data can be appended later on
numlist = []


# reading through each line in the file
for line in fhandle:
    line = line.rstrip() # removing spaces between lines
    extract = re.findall("([0-9]+)", line) # using regex 'greedy' to extract nos
    if len(extract) < 1 : continue
    print(extract)

# For loop inside: for each line extracted above the, the below For loop will
# append the numbers to a list, namely numlist
    for i in range(len(extract)):
        num = float(extract[i])
        numlist.append(num)

print(sum(numlist))
