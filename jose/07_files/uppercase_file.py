"""
Code that prompts for a file name, then opens that file 
and reads through the file, and print the contents of 
the file in upper case. Use the file words.txt

"""

#prompts for a file name
f_name=input("Please enter the file name: ")

#checks file name 
try:
	f_hand=open(f_name)
except:
	print("Error!",f_name,"not found.")
	quit()

#prints in upper case
for line in f_hand:
	fin=line.strip().upper()
	print(fin)
	#print("asdfaskdjfhqlwSABFKSJHFKJHBF")
