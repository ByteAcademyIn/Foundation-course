'''
program to calculate score between 0.0 and 1.0
written by Lebo

'''

#Input score

score = float (input ('Enter a score between 0.0 and 1.0: '))

#Out of range score

if 0.0 <= score <= 1.0:

#Grading
    if score >= 0.9:
        print ('A')
    elif score >= 0.8:
        print ('B')
    elif score >= 0.7:
        print ('C')
    elif score >= 0.6:
        print ('D')
    else:
        print ('F')

#Out of range condition
        
else:
    print ('Error: out of range')
