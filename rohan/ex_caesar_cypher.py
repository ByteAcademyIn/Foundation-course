'''
A Caesar cypher is a weak form of encryption that involves “rotating” each
letter by a fixed number of places. To rotate a letter means to shift it
through the alphabet, wrapping around to the beginning if necessary, so ’A’
rotated by 3 is ’D’ and ’Z’ rotated by 1 is ’A’. To rotate a word, rotate each
letter by the same amount. For example, “cheer” rotated by 7 is “jolly” and
“melon” rotated by -10 is “cubed”. In the movie 2001: A Space Odyssey, the
ship computer is called HAL, which is IBM rotated by -1. Write a function
called rotate_word that takes a string and an integer as parameters, and
returns a new string that contains the letters from the original string
rotated by the given amount. You might want to use the built-in function ord,
which converts a character to a numeric code, and chr, which converts numeric
codes to characters.
'''

#defining the rotate_word function
def rotate_word(word, shift):

    #initializing variable to store the encrypted word
    new_word = None

    #creating a new word
    for i in word:
        #getting the character value
        letter_value = ord(i)

        #checking if the character is an alphabet
        if not (((letter_value >= 65) and (letter_value <= 90)) or ((letter_value >= 97) and (letter_value <= 122))):
            #leaving the character unchanged if not an alphabet
            shifted_letter_value = letter_value

           #shift for uppercase letters
        elif (letter_value >= 65) and (letter_value <= 90):
            shifted_letter_value = letter_value + shift

            #starting from 'Z' if the value is lesser than 'A'
            if not ((shifted_letter_value >= 65)):
                while not (shifted_letter_value >= 65):
                    x = 65 - shifted_letter_value
                    shifted_letter_value = 91 - x

            #starting from 'A' if the value is greater than 'Z'
            if not ((shifted_letter_value <= 90)):
                while not (shifted_letter_value <= 90):
                    y = shifted_letter_value - 90
                    shifted_letter_value = 64 + y

            #shift for lowercase letters
        elif (letter_value >= 97) and (letter_value <= 122):
            shifted_letter_value = letter_value + shift

            #starting from 'z' if the value is lesser than 'a'
            if not ((shifted_letter_value >= 97)):
                while not (shifted_letter_value >= 97):
                    x = 97 - shifted_letter_value
                    shifted_letter_value = 123 - x

            #starting from 'a' if the value is greater than 'z'
            if not ((shifted_letter_value <= 122)):
                while not (shifted_letter_value <= 122):
                    y = shifted_letter_value - 122
                    shifted_letter_value = 96 + y




        #converting the new unicode value to a character
        new_letter = chr(shifted_letter_value)

        #making sure new_word is not unassigned
        if new_word is None:
            new_word = new_letter

        else:
            #concatenating each letter to form the rotated word
            new_word = new_word + new_letter

    return new_word

#input prompts for word and shift value
word = input('Enter a word: ')
shift = int(input('Enter a shift value: '))

#Test cases for Caesar Cypher:
#assert rotate_word('AbCd', -3) == 'XyZa', "Incorrect encryption"
#assert rotate_word('ZyXw', -100) == 'DcBa', "Incorrect encryption"
#assert rotate_word('ZyXw', 100) == 'VuTs', "Incorrect encryption"
#assert rotate_word('ZyXw', 22) == 'VuTs', "Incorrect encryption"
#assert rotate_word('I am 100% awesome', -3) == 'F xj 100% xtbpljb', "Incorrect encryption"
#printing encrypted word
print(rotate_word(word, shift))
