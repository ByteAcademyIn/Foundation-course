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


"""
Remarks:
1. Have the proper question at the beginning of the program
2. Be consistent with tabs and spaces
3. Either use 'exit()' in the except block or have the calculation in try block
Your program tries to execute even if I enter random characters.

Score: 12/10
"""
