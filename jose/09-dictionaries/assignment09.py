"""
Write a program to read through the mbox-short.txt 
and figure out who has the sent the greatest number 
of mail messages. The program looks for 'From ' lines 
and takes the second word of those lines as the person
who sent the mail. The program creates a Python dictionary 
that maps the sender's mail address to a count of the number 
of times they appear in the file. After the dictionary is 
produced, the program reads through the dictionary using a 
maximum loop to find the most prolific committer.

Desired output: cwen@iupui.edu 5
"""

#prompts input
name = input("Please enter the file:")

if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)

#creating an empty dictionary
count = dict()

# dictionary with counts
for line in handle:
    word = line.split()
    if line.startswith("From "):
        count[word[1]] = count.get(word[1], 0) + 1

# finds the prolific committer and commits
big_count = 0
big_id = ""
for k in count:
    if count[k] > big_count:
        big_count = count[k]
        big_id = k

#prints output
print (big_id,big_count)
