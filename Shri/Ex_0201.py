#If else function for total pay

hours = input ("How many hours of work:")
try:
    Workinghours = float(hours)
except:
    Workinghours = -1

if Workinghours > 0:
    print("nice work")
else:
    print("Error! Pls. enter numeric value")


Pay = input ("rate of pay per hour:")
try:
    Payperhour = float(Pay)
except:
    Payperhour = -1

if Payperhour > 0:
    print("nice work")
else:
    print("Error! Pls. enter numeric value")


if Workinghours <=40:
    print(Workinghours*Payperhour)
else:
    print((40*Payperhour) + (Workinghours-40)*Payperhour*1.5)
