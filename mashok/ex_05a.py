""" Ask the user to input numbers when prompted. Once the user enters 'done'
calculate the total, average and count. """
sum = 0 # initialising a while loop starting with zero
count = 0 

while True:
    say = input("enter a number: ")
    if say == 'done' :
        break # This breaks the loop
    try:
        say_num = int(say)
        sum = sum + say_num # a store for the total
        count = count + 1 # a store for the number of inputs
    except ValueError: # creating an exception type for error in value type
        print("invalid data")
print(sum, count, sum/count)
