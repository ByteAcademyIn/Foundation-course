# total working hours to be caculated.

workinghours= input('enter the number of workinghours: ')
rph= input('enter the rph ')

hours= float(workinghours)
rph= float(rph)

if hours <= 40:
  print(hours*rph)
else :
 print((rph*40)+(hours-40)*rph*1.5)
