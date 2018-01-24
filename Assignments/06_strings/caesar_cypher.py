""" THIS IS A PROGRAM WHICH SHIFTS A CHARACTER BY A CERTAIN PLACES - CEASAR CYPHER CONCEPT"""

#Taking Input from the User

original = raw_input(" Please Enter the word to be coded ")
original=original.strip()
num = raw_input (" Please enter the shift number ")
num=int(num)
coded_msg=''
#Try and Except method to ensure correct input
#coded_msg=[char for char in original]
#print(coded_msg)
#for char in coded_msg :
    #print(char)
try:
    x=int(original)
    print (" This is serious Business - Dont fool around - Enter the correct value ")
    exit()
except:
    print ( " Good Job - May The Force Be With You ... The Eagle has landed -- see below " )
    original = str(original)

# defining a function called encryption to encrypt the user input as per ceasar cypher
def encryption(original, num) :
# adjusting shift as per positive and negative inputs and within a-z/A-z
    if num <0 :
        num= (-1) * (num % 26)
    else : num = num%26
    #print(num)

# adjusting out of bound case for capital & Small case letters -
    for char in original :
        #print(char)

# 1st gate to ensure the characters being changed are in 26 character range (eg 100% will remain 100%)
        if ((ord(char)<65 and ord(char)>90)) and ((ord(char)<97 and ord(char)>122)) :
            coded_msg=coded_msg + char
            continue
            #print(char)
#2nd gate to check for outof bound capital letters after shifting
        if (ord(char) + num <65) and (ord(char)+ num < 97) :
            char=chr(ord(char)+26)
            #print(char)
        elif (ord(char) + num >90) and (ord(char)+ num >122) :
            char=chr(ord(char)-26)
# shifting the character as per the shift number provided
        elif char=chr(ord(char)+num) :
        #print(char)
        coded_msg = coded_msg + char
    return coded_msg

print (encryption(original,num))



#obsolete
#Please ignore below this point...

"""
    temp = ''
    for letter in original:
        if letter == 'z'and num>0 :
            letter='a'
            temp += chr(ord(letter)+(num-1))
            continue

        elif letter == 'Z' and num>0 :
            letter='A'
            temp += chr(ord(letter)+(num-1))
            continue

        temp += chr(ord(letter)+num)

    print(temp)
"""
