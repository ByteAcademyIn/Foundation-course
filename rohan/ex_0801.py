'''
Open the file romeo.txt and read it line by line. For each line, split the
line into a list of words using the split() method. The program should build a
list of words. For each word on each line check to see if the word is already
in the list and if not append it to the list. When the program completes, sort
and print the resulting words in alphabetical order.

Desired Output:

['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east',
'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick',
'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']
'''

#input prompt
filename = input('enter a file path: ')
if filename == '':
    filename = '/Users/rohandatar/Foundation-course/Assignments/08-lists/romeo.txt'

#opening the file
file = open(filename)

#initializing the list of words in the file
all_words = list()

#iterating through the lines in the file
for line in file:
    line = line.strip()

    #spliting the line into words
    line_words = line.split()

    #iterating over the words in the line
    for word in line_words:
        #checking if the word is already in the list and
        if word not in all_words:
            all_words.append(word)


#printing the sorted list
all_words.sort()
print(all_words)
