"""
Write code using find() and string slicing to extract the number 
at the end of the line below. Convert the extracted value to a 
floating point number and print it out.

text = "X-DSPAM-Confidence: 0.8475"
"""

#prompts to enter the data
data=input("Please enter the data: ")

#finds the position to extract 
f_pos=data.find(":")

#extracting the number from the data
num=data[f_pos+1:]

#prints the number
print("Number:",float(num))