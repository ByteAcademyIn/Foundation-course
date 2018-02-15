# Rewriting the program using try and except

hours= input('enter hours: ')
rate= input('enter rate: ')



try:
   hours= float(hours)
   rate= float(rate)
   print('nice work')
except:
    print('error in numeric input')

if hours <= 40:
  print(hours*rate)
else :
 print((rate*40)+(hours-40)*rate*1.5)
