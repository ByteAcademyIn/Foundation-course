"""
Open the file romeo.txt and read it line by line. 
For each line, split the line into a list of words 
using the split() method. The program should build 
a list of words. For each word on each line check 
to see if the word is already in the list and if not 
append it to the list. When the program completes, 
sort and print the resulting words in alphabetical order.

Desired Output:

['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and',
 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill',
  'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the',
   'through', 'what', 'window', 'with', 'yonder']
"""

#creating an empty list
words=list()

#prompts for a file name
f_name=input("Please enter the file name: ")

#checks file name 
try:
	f_hand=open(f_name)
except:
	print("Error!",f_name,"not found.")
	quit()

#spliting the lines into a list of words
for line in f_hand:
	for word in line.split():
		if word not in words:
			words.append(word)

#sorting words
words.sort()

#printing words
print(words)

	