'''
Write a program that prompts for a file name, then opens that file and reads
through the file, and print the contents of the file in upper case. Use the
file words.txt
'''

#input prompts
filename = input('Enter a file name/path: ')

#opening file in read mode
file = open(filename, 'r')

#iterating through the lines in a file
for line in file:

    #printing each line in uppercase
    print(line.upper(), end='')
