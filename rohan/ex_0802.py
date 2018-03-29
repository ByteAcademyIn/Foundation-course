'''
Open the file mbox-short.txt and read it line by line. When you find a line
that starts with 'From ' like the following line: From
stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008 You will parse the From
line using split() and print out the second word in the line (i.e. the entire
address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.

Desired Output:

stephen.marquard@uct.ac.za louis@media.berkeley.edu zqian@umich.edu
rjlowe@iupui.edu zqian@umich.edu rjlowe@iupui.edu cwen@iupui.edu cwen@iupui.edu
gsilver@umich.edu gsilver@umich.edu zqian@umich.edu gsilver@umich.edu
wagnermr@iupui.edu zqian@umich.edu antranig@caret.cam.ac.uk
gopal.ramasammycook@gmail.com david.horwitz@uct.ac.za david.horwitz@uct.ac.za
david.horwitz@uct.ac.za david.horwitz@uct.ac.za stephen.marquard@uct.ac.za
louis@media.berkeley.edu louis@media.berkeley.edu ray@media.berkeley.edu
cwen@iupui.edu cwen@iupui.edu cwen@iupui.edu There were 27 lines in the file
 with From as the first word
 '''

#input prompt
filename = input('enter a file path: ')
if filename == '':
    filename = '/Users/rohandatar/Foundation-course/Assignments/07_files/mbox-short.txt'

#opening the file
file = open(filename)

#initializing list of emails and the counter
emails = list()
count = 0

#iterating over the lines of the file
for line in file:

    #checking if the line is in the line
    if 'From ' in line:

        #splitting the line into words
        words = line.split()

        #appending the second word to the list
        emails.append(words[1])

        #incrementing the counter
        count += 1

#printing the emails
for i in range(len(emails)):
    print(emails[i], end = ' ')

print('There were', (len(emails)), 'lines in the file with From as the first word')
