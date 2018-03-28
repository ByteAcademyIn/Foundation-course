'''
Write code using find() and string slicing to extract the number at the end of
the line below. Convert the extracted value to a floating point number and
print it out.

text = "X-DSPAM-Confidence: 0.8475"
'''

#input prompt
text = input('enter text: ')

#Finding the number
x = text.find(':')

#extracting the number
num = text[x+1:]

#Printing the floating point number
print(float(num))
