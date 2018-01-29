"""
Creating a list of unique words in a given text
"""

# Ask the user to enter the file name and open the file handle
fname = input("Please enter the file name: ")
fhandle = open(fname)

list_of_words = []

# Iterate over each line in the file
for line in fhandle:

    # Split the line into a list of words
    words = line.strip().split()

    #Iterate over each word in the line
    for word in words:

        #If the word is not in the list of unique words, append it
        if word not in list_of_words:
            list_of_words.append(word)

# Print the sorted list of words
list_of_words.sort()
print(list_of_words)
