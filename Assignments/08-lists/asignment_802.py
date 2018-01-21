

"""Open the file mbox-short.txt and read it line by line. When you find a line that starts with
'From ' like the following line: From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008 You
will parse the From line using split() and print out the second word in the line (i.e. the
entire address of the person who sent the message). Then print out a count at the end. Hint:
 make sure not to include the lines that start with 'From:'.
Desired Output:
stephen.marquard@uct.ac.za louis@media.berkeley.edu zqian@umich.edu.
There were 27 lines in the file with From as the first word"""

filename = raw_input ( " Please Enter the File Name " )
fhandle = open (filename)
count=0
email = list()
for line in fhandle:
    line=line.strip()
    if not line.startswith('From') :
        continue
    count=count+1
    temp=line.split()
    email=temp[1]
print ( " there were total of " , count , " line starting with From " )
print ( email)
