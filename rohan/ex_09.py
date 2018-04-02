'''
Write a program to read through the mbox-short.txt and figure out who has the
sent the greatest number of mail messages. The program looks for 'From ' lines
and takes the second word of those lines as the person who sent the mail. The
program creates a Python dictionary that maps the sender's mail address to a
count of the number of times they appear in the file. After the dictionary is
produced, the program reads through the dictionary using a maximum loop to find
the most prolific committer.

Desired output: cwen@iupui.edu 5
'''

#input prompt
filename = input('Enter a file name: ')
if filename == '':
    filename = '/Users/rohandatar/Foundation-course/Assignments/07_files/mbox-short.txt'

#opening the file
file = open(filename)

#initializing the dictionary
emailid = dict()

#iterating through the file
for line in file:
    #checking if the line starts with 'From '
    if 'From ' in line:
        words = line.split()

        #counting the number of times the email appears using get()
        emailid[words[1]] = emailid.get(words[1], 0) + 1

#initializing the variables to store the most common email and the number of instances
most_emails = None
number_of_emails = None

#iterating over the dictionary items
for id, count in emailid.items():
    #checking if the current item has the highest value
    if (number_of_emails is None) or (number_of_emails < count):
        most_emails = id
        number_of_emails = count


#printing the most common sender and the number of emails they sent
print(most_emails, number_of_emails)
