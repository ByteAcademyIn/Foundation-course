#Creating a score report

inp = input ("Enter a number between 0.0 and 1.0")
score = float(inp)

if (score >=1.0):
print ( "You didnt follow instructions")
quit()

elif (score >=0.9):
print("A")
elif (score >=0.8):
print("B")
elif (score >=0.7):
print("C")
elif (score >=0.6):
print("D")
else:
print("F")

except:
print("please enternumerical numbers")
quit()
