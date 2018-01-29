"""Write a program that prompts for a file name, then opens that file and reads through the
file, and print the contents of the file in upper case. Use the file words.txt"""

# printing the menu for program
print ( " Enter 1 to convert all lines in a file to upper case " )
print ( " Enter 2 to Quit the program " )
option = raw_input( " please enter your choice " )
# checking the user input
if option == 1 :
    fhandle= open ("words.txt")
    temp=str()
    for line in fhandle:
        temp=line.upper()
        print(temp)

# checking if user wants to quit the program.
elif option == 2 :
    exit()
