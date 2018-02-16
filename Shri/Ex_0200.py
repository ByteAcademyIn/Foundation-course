#If else function for total pay

hours = input ("How many hours of work:")
Pay = input ("rate of pay per hour:")

Workinghours = float(hours)
Payperhour = float(Pay)

if Workinghours <= 40:
    print(Workinghours*Payperhour)
else :
    print((40*Payperhour) + (Workinghours-40)*Payperhour*1.5)
