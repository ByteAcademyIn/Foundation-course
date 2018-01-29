import re

# Ask the user for the file name and open the file
file_name = input("Please enter the file name:")
# Providing a default file name
if len(file_name)<1: file_name = 'regex_sum_test.txt'

# Extracting the numbers from the file and summing them
print(sum([int(num) for num in re.findall('[0-9]+',open(file_name, 'r').read())]))
