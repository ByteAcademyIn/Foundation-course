"""
Write a program to read through the mbox-short.txt and 
figure out the distribution by hour of the day for each 
of the messages. You can pull the hour out from the 'From ' 
line by finding the time and then splitting the string a second 
time using a colon. From stephen.marquard@uct.ac.za Sat Jan 5 
09:14:16 2008 Once you have accumulated the counts for each hour, 
print out the counts, sorted by hour as shown below.

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
"""

#prompts input
name = input("Please enter the file:")

if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)

#creating an empty dictionary
counts = dict()

for line in handle:
    if line.startswith("From "):
        time = line.split()[5].split(":")
        counts [time[0]] = counts.get(time[0], 0) + 1


#creating an empty list
list = list()

# appends and sorts
for key, value in counts.items():
    list.append( (key,value) )

#prints output
for hour, counts in sorted(list):
    print (hour, counts)