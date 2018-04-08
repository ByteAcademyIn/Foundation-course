"""
A Caesar cypher is a weak form of encryption that involves 
“rotating” each letter by a fixed number of places. To rotate 
a letter means to shift it through the alphabet, wrapping 
around to the beginning if necessary, so ’A’ rotated by 3 
is ’D’ and ’Z’ rotated by 1 is ’A’. To rotate a word, 
rotate each letter by the same amount. For example, “cheer” 
rotated by 7 is “jolly” and “melon” rotated by -10 is “cubed”. 
In the movie 2001: A Space Odyssey, the ship computer is 
called HAL, which is IBM rotated by -1. Write a function 
called rotate_word that takes a string and an integer as 
parameters, and returns a new string that contains the letters 
from the original string rotated by the given amount. 
You might want to use the built-in function ord, which 
converts a character to a numeric code, and chr, which 
converts numeric codes to characters.
"""

# prompts for inputs
word=input("Please enter the word to be cyphered: ")
key=int(input("Please enter the key: "))

#function cyphers letter one at a time
def rotate_letter(x, key):
   
   	#if an upper case letter
    if x.isupper():
        letter=ord(x)+key

        #if the value is lesser than 65
        if letter<65: 
            while letter<65:
                letter=letter+26
            
        #if the value is greater than 90
        elif letter>90: 
            while letter>90:
                letter=letter-26
    
    #if a lower case letter            
    elif x.islower():
        letter=ord(x)+key

        #if the value is lesser than 97
        if letter<97: 
            while letter<97:
                letter=letter+26
            
        #if the value is greater than 122
        elif letter>122: 
            while letter>122:
                letter=letter-26

    # if niether uppercase nor lower case    
    else:return x

    #returns the character equivalent
    return chr(letter)
    
#fuction to bind the letters
def rotate_word(word, key):
    
    #initialising result
    result=""

    #binding the letters together and returns
    for x in word:
        result+=rotate_letter(x, key)
    return result

# prints the output
print("Cyphered word:",rotate_word(word, key))

#Test cases for Caesar Cypher:
assert rotate_word('AbCd', -3) == 'XyZa', "Incorrect encryption"
assert rotate_word('ZyXw', -100) == 'DcBa', "Incorrect encryption"
assert rotate_word('ZyXw', 100) == 'VuTs', "Incorrect encryption"
assert rotate_word('ZyXw', 22) == 'VuTs', "Incorrect encryption"
assert rotate_word('I am 100% awesome', -3) == 'F xj 100% xtbpljb', "Incorrect encryption"

