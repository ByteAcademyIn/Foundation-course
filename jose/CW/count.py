"""Count the charaters in a word"""


# Prompt the word
word=input("Enter the word:")

#For loop function to count
def count_fuc(wrd):

	count=0
	for x in wrd:
		count=count+1
	return count

print(count_fuc(word))



