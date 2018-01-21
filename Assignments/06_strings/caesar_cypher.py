


original = raw_input(" Please Enter the word to be coded ")
num = raw_input (" Please enter the shift number ")
num=int(num)
try:
    x=int(original)
    print (" This is serious Business - Dont fool around - Enter the correct value ")
    exit()

except:
    print ( " Good Job - May The Force Be With You ... The Eagle has landed -- see below " )
    original = str(original)

temp = ''
for letter in original:
    if letter == 'z'and num>0 :
        letter='a'
        temp += chr(ord(letter)+(num-1))
        continue

    elif letter == 'Z' and num>0 :
        letter='A'
        temp += chr(ord(letter)+(num-1))
        continue

    temp += chr(ord(letter)+num)

print(temp)
