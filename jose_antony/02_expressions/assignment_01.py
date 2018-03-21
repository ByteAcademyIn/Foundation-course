#prompts the user to enter no. of hours
hours=input("Please enter the no. of hours: ")

#prompts the user to enter rate per hour
rate=input("Please enter your rate per hour: ")

#Computing the gross pay
pay=float(hours)*float(rate)

#Prints the gross pay
print("Gross pay is: ",pay)
