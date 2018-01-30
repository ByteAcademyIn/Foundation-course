# find the maximum and minimum for n-1 numners (n beign the number count input from user )

# taking count from user
num=int(input ( " Please enter the count of numners : "))
#taking user input
num_list=[float(x) for x in input( " Please Enter the Numbers").split()]
#sorting in ascending order
num_list.sort()
#defining a function to calculate the minimumand maximum for n-1 numbers
def calc(num, num_list) :
    print (num_list)
    max_s=0
    min_s=0
#calculating and printing maximuma nd minimum sums 
    for i in range(len(num_list)-1):
        max_s+= num_list[i]
        min_s+=num_list[num-1-i]
    print(max_s , min_s)
calc(num, num_list)
