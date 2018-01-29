

""" Write a program to read through the mbox-short.txt and figure out who has the sent the greatest
number of mail messages. The program looks for 'From ' lines and takes the second word of those
lines as the person who sent the mail. The program creates a Python dictionary that maps the
sender's mail address to a count of the number of times they appear in the file. After the dictionary
is produced, the program reads through the dictionary using a maximum loop to find the most prolific
committer.

Desired output: cwen@iupui.edu 5 """



#Taking User Input
filename = raw_input ( " Please enter the File Name ")
fhandle= open(filename)

email=''
x=[]
dictionary=dict()
count=0
#Adding all the emails and their respective counts in a dictionary
for line in fhandle :
    line=line.strip()

    if line.find('From')==0:
        #print(line)
        x = line.split(' ')
        #print(x)
        temp=x[1]
        #print(temp)


        if temp not in dictionary :
            dictionary[temp]=1

        else :
            dictionary[temp]= dictionary[temp]+1
#print(dictionary)

#finding the maximum value in dictionary
for email in dictionary :
    if dictionary[email] > count :
        temp=email
        count=dictionary[email]

print ( " Maximum Emails were sent by below mentioned user : ")
print ( temp,dictionary[temp])
