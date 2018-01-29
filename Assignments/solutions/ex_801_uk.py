"""Open the file romeo.txt and read it line by line. For each line, split the line into a list
of words using the split() method. The program should build a list of words. For each word on
each line check to see if the word is already in the list and if not append it to the list. When
 the program completes, sort and print the resulting words in alphabetical order."""

filename = raw_input ( " Please enter the file name " )
fhandle=open(filename,'r')
temp=list()
for line in fhandle :
    words=line.strip().split()
    for word in words :
        if word not in temp :
            temp.append(word)
            continue
        else:
            continue
temp.sort()
print ( temp )
