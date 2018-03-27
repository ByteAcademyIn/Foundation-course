


def length(st):
    count=0
    while True:

        try:
            x=st[count]
        except:
            break
        count= count+1
    return count

s = input('enter a word ')
print(length(s))
