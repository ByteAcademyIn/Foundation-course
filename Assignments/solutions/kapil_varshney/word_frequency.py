"""
Print the 5most common words in a file and find the frequency.

"""

# Ask the user for file name.
file_name = input('Please enter the file name: ')
# Providing a default filename
if len(file_name) <1 : file_name='clown.txt'

word_freq = {}

fhandle = open(file_name)

#Iterate over each line in the file
for line in fhandle:
    #print (line)
    words = line.strip().split()
    #print (words)

    for word in words:
        word_freq[word] = word_freq.get(word, 0)+1
    #print (word_freq)

'''
freq_list = []
for k, v in word_freq.items():
    freq_list.append((v,k))

#freq_list.sort(reverse = True)
sorted_list = sorted(freq_list, reverse = True)
for k, v in sorted_list[:5]:
    print (k, v)
'''

print (sorted([(v,k) for k, v in word_freq.items()], reverse = True)[:5])
