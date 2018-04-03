'''
Write a program to read through the mbox-short.txt and figure out the
distribution by hour of the day for each of the messages. You can pull the hour
out from the 'From ' line by finding the time and then splitting the string a
second time using a colon. From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16
2008 Once you have accumulated the counts for each hour, print out the counts,
sorted by hour as shown below.

Desired Output:

04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
'''

#input prompts
filename = input('Enter a file path: ')
if filename == '': filename = '/Users/rohandatar/Foundation-course/Assignments/07_files/mbox-short.txt'

#opening the file
file = open(filename)

#initializing a dictionary for the hours
hours = {}

#iterating over the lines in the file
for line in file:

    #finging the 'From lines'
    if 'From ' in line:

        #splitting the line into words
        words = line.split()

        #splitting the time
        time = words[5].split(':')

        #using get method to count the number of times the hour appears
        hours[time[0]] = hours.get(time[0],0) + 1


#printing the hours in order
for h, c in sorted(hours.items()):
    print(h,c)
