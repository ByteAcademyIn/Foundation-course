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

        #finding the unicode value of each letter and incrementing it by shift
        shifted_letter_value = ord(i) + shift

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

#printing encrypted word
print(rotate_word(word, shift))
