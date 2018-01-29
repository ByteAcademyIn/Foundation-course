"""
This is a program to rotate words by a given number as in Caesar Cypher.
"""

#Take user input for the text and the rotation integer
#msg = input("Please enter the message to be encrypted: ")
#shift = int(input("Please enter the encryption key: "))


def rotate_word(msg, shift):

    # get the shift within 26
    # If the shift is a negative number, make sure not to mess up
    shift = shift%26
    new_msg = ''
    # Get rid of whitespaces
    msg = msg.strip()

    # Iterate over each charachter in th text
    for char in msg:
        # Capital case
        if ord(char)>=65 and ord(char)<=90:
            # Shift the character
            new_char = ord(char)+shift
                # Check if the new char goes out of bound and cycle it back
            if new_char<65:
                new_char = new_char+26
                #print ("<65")
            elif new_char>90:
                new_char = new_char-26
                #print(">90")
        # Small case
        elif ord(char)>=97 and ord(char)<=122:
            new_char = ord(char)+shift
            if new_char<97:
                new_char = new_char+26
                #print("<97")
            elif new_char>122:
                new_char = new_char-26
                #print(">122")
        else:
            new_char = ord(char)

        #Append the rotated charachters to the new msg
        final_char = chr(new_char)
        new_msg = new_msg+final_char

    #Return the final encrypted msg
    print (new_msg)
    return new_msg

#print (rotate_word(msg, shift))

assert rotate_word('AbCd', -3) == 'XyZa', "Incorrect encryption"
assert rotate_word('ZyXw', -100) == 'DcBa', "Incorrect encryption"
assert rotate_word('ZyXw', 100) == 'VuTs', "Incorrect encryption"
assert rotate_word('ZyXw', 22) == 'VuTs', "Incorrect encryption"
assert rotate_word('I am 100% awesome', -3) == 'F xj 100% xtbpljb', "Incorrect encryption"
#assert decrypt('VuTs', 22) == 'ZyXw', "Incorrect encryption"
