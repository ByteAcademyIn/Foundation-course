#Input from user for score
score = float(input("Enter the score: "))

#Checking whether the number is in the specified range or not

if(score <= 0.0):
  print("Error: Out of range ")
  exit()
if(score >= 1.0):
  print("Error: Out of range ")
  exit()

#Printing the respective grades for score entered
if(score >= 0.9):
  print("Grade is: A")
elif(score >= 0.8):
  print("Grade is: B")
elif(score >= 0.7):
  print("Grade is: C")
elif(score >= 0.6):
  print("Grade is: D")
else:
  print("Grade is: F")
