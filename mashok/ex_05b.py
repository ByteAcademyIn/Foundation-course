""" /Ask the user to enter numbers when prompted, when the user enters 'done'
terminate and print out the largest number and the smallest numbers """

big = 0  # initialising the while loop with a zero
small = 0
while True:
    say = input("enter a number: ")
    if say == 'done' :
        break # break the loop when user enters 'done'
    try:
        say_num = int(say)
        if say_num == 0 or say_num > big :
            big = say_num # storing the biggest number
        if say_num == 0 or say_num < small :
            small = say_num # storing the smallest number
    except ValueError: # exception error captured for wrong value type
        print("only numbers here, else type 'done' to exit")
print(big, small) # print results
