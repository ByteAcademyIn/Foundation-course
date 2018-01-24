#takignthe size of staircase from user
size=int(input( ' Please Enter the Size of the staircase : ' ) )
symbol= str(input (' please enter the symbol for creating the staircase : '))

stair=[[symbol]* size for i in range(size)]
for i in range(size) :
    for j in range(size-i-1) :
        stair[i][j]=' '
for i in stair:
    for i in i:
        print(i, end= ' ')
    print()
#print('\n'.join(stair))
