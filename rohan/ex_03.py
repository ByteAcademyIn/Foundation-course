'''
Question:
Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is
between 0.0 and 1.0, print a grade using the following table:
Score Grade
0.9 =< A
0.8 =< B
0.7 =< C
0.6 =< D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit.
'''

#Input prompt
score = input('Enter a score between 0.0 and 1.0: ')

#Data type check
try:
    s = float(score)
    #range check
    if s > 1.0 :
        print('Error: score not in range')
        exit()
    elif s < 0 :
        print('Error: score not in range')


    #Convert to grade
    elif s < 0.6 :
        print('F')
    elif s < 0.7 :
        print('D')
    elif s < 0.8 :
        print('C')
    elif s < 0.9 :
        print('B')
    elif s <= 1.0 :
        print('A')

except:
    print('Error: enter numeric data')
    exit()
