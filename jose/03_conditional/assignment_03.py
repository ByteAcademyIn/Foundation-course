"""
Code to prompt for a score between 0.0 and 1.0. 
If the score is out of range, print an error. 
If the score is between 0.0 and 1.0, 
print a grade using the following table:
Score Grade
0.9 =< A s>=9
0.8 =< B
0.7 =< C
0.6 =< D
< 0.6 F
If the user enters a value out of range, 
print a suitable error message and exit.

"""
# prompts the user to enter a score between 0.0 and 1.0
score=input("Please enter a score between 0.0 and 1.0 : ")

# Checking if non-numeric value
try : 
	score_check = float(score) 

	# Checking if values between 0.0 and 1.0
	 
	if (score_check > 1.0) :
		print("Error! Please enter a score between 0.0 and 1.0.")

	# Score grading
	elif score_check >= 0.9 : 
		grade = "A"
	elif score_check >= 0.8 : 
		grade = "B"
	elif score_check >= 0.7 : 
		grade = "C"
	elif score_check >= 0.6 : 
		grade = "D"
	elif score_check < 0.6 : 
		grade = "F"

	print("Grade :",grade)

		
except :
	print("Error! Please enter a score between 0.0 and 1.0.")
