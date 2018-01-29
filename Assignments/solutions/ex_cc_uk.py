""" THIS IS A PROGRAM WHICH SHIFTS A CHARACTER BY A CERTAIN PLACES - CEASAR CYPHER CONCEPT"""

#Taking Input from the User

original = input(" Please Enter the word to be coded ")
original=original.strip()
num = input (" Please enter the shift number ")
num=int(num)
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
    code=''

# adjusting shift as per positive and negative inputs and within a-z/A-z
    if num <0 :
        num= (-1) * (num % 26)
    else : num = num%26
    #print(num)

# adjusting out of bound case for capital & Small case letters -
    for char in original :

#capital case
        if ord(char)>=65 and ord(char)<=90:
            coded_msg=ord(char)+num
            if coded_msg<65 :
                coded_msg=coded_msg+26
            elif coded_msg>90 :
                coded_msg=coded_msg-26
# small case
        elif ord(char)>=97 and ord(char)<=122:
            
            coded_msg= ord(char)+num
            #print(coded_msg)
            if coded_msg<97 :
                coded_msg=coded_msg+26
            elif coded_msg>122 :
                coded_msg=coded_msg-26
        coded_msg=chr(coded_msg)
        code = code+coded_msg

    return(code)

print(encryption (original, num))
