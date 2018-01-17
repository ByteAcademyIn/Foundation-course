"""This is a program to prompt for a score between 0.0 and 1.0.
If the score is out of range, print an error.
If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade = 0.9 A = 0.8 B = 0.7 C = 0.6 D < 0.6 F
If the user enters a value out of range, this program wil print a suitable
error message and exit."""

#inputting score from user
score=input("Please enter the Score, given by the committee")

#assigning float calss to input variable
try:
    score=float(score)
except:
    print("This score was not provided by the committee; Kindly restart and enter the score between 0-1")
    exit()

#categorizing & printing the score as per grade specification

if score==0.9 :
    grade="Your Grade is A  Well Done!! "
elif score==0.8 :
    grade="Your Grade is B  Well Done!! "
elif score==0.7 :
    grade="Your Grade is C  Good Effort!! "
elif score==0.6 :
    grade="Your Grade is D  You have potential !! "
elif score<0.6 and score>0 :
    grade="Your Grade F  when there is a will there is a way!! "
else :
    grade="We appreciate your efforts however your score doesnot satisfy our grading criteria - Kindly try again :) "
print (grade)
exit()
