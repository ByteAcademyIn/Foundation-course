""" Write a program to read through the mbox-short.txt and find out who has
sent the greatest number of email messages"""

# opening and  reading the file
name = input("enter a file name: ")
handle = open(name)

# creating a dictionary
count = dict()


# reading each line that starts with "From" and splitting the lines into a list
for line in handle:
        if line.startswith('From '):
            word = line.split()
            count[word[1]] = count.get(word[1], 0) + 1
            # this adds to the dictionary only the email addresses
            # the dictionary also counts the key instances


""" looping through the dictionary and finding which is the email address that
appears the most """
largest = 0
email = ''
for k in count:
    if count[k] > largest:
        largest = count[k]
        email = k
print(largest, email)
