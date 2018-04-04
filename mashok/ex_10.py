""" write a program to read the mbox short txt file and find out the distribution
of messages by the hour """


# to open and read the file
name = input("enter file name: ")
handle = open(name)

# initiate a dictionary
counts = dict()

# using for loop to read through each line of the file
for line in handle:
# extracting lines starting with 'From'
    if line.startswith("From "):
# splitting the line into a list
        time = line.split()
#  extracting another list from the fifth element which is the time, splitting
# it at the ":" separator
        hour = time[5].split(":")
# from the above list, time is added to the dictionary, the count is also made
        counts[hour[0]] = counts.get(hour[0], 0) + 1


# converting the dictionary into a tuple so that it can be sorted
tup = list() # intiating the tuple

# creating and looping through the tupple so that keys, values can be appended
for key, value in counts.items() :
    tup.append((key, value))
# sorting the tupple based on time
tup.sort()
# printing the key, value pair in the tupple in separate lines (contd)
# (contd) by using loop function
for hours, counts in tup:
    print(hours, counts)
