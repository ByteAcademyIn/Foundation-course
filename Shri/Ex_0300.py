def computepay (hours,Pay):

    Workinghours = float(hours)
    Payperhour = float(Pay)

    if Workinghours <=40:
        print(Workinghours*Payperhour)
    else:
        print((40*Payperhour) + (Workinghours-40)*Payperhour*1.5)
        return computepay


hours = input ("How many hours of work:")
Pay = input ("rate of pay per hour:")

computepay (hours, Pay);
