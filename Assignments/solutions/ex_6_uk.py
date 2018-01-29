

""" Write code using find() and string slicing to extract the number at the end of the line below.
Convert the extracted value to a floating point number and print it out.
text = "X-DSPAM-Confidence: 0.8475 """
# the solution specific to this assignment has been answered in option-1 

# printing the instructions and taking Input
print ( " This Program extracts the float value from entered line")
print (" Press-1 to illustrate an example " )
print ( " Press-2 to use program ")

option= input ( " Enter your choice now " )
option= int(option)

if option==2 :
    print ( " ONLY enter ': ' before decimal start & after the complete number in the Line " )
    line = raw_input( " Please enter the Line " )
    line=str(line)

# finding the starting & ending point of the number in line.
    start_pos=line.find(':')+1
    end_pos = len(line)

    temp = line[start_pos:end_pos]
    end_pos= temp.find(':')
#printing the sliced string containing the number
    print ( " the numbers in the line are :  " )
    print (temp[:end_pos])

elif option==1 :
    print (" the line is  X-DSPAM-Confidence: 0.8475  ")
    line= '-DSPAM-Confidence: 0.8475'
    pos = line.find(':')
    print ( 'the number extracted from the line is' )
    x = float(line[pos+2:len(line)])
    print(x)
