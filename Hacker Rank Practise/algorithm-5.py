# sum of both diagonals
d1=[]
d2=[]

# Assigning the sum variables as 0
d1_sum=0
d2_sum=0

#inputting matrix size
n=int(input( " Enter the matrix size n X n : "))

#inputting matrix
matrix=[[int(j) for j in input( " please enter the row " ).split()] for i in range(n)]

# finding sum of diagonals and storing diagonals in respective lists
for i in range(n):
    d1.append([matrix[i][i]])
    d1_sum+=matrix[i][i]
    d2.append([matrix[n-i-1][i]])
    d2_sum+=matrix[n-i-1][i]
# ask ? how to convert 2d list into 1 day list in one line. ( for above case i want to use sum())

#printing the output
for i in matrix:
    for i in i:
        print ( i , end= ' ' )
    print()

print( '\n Sum of Diagonal' , d1 , 'is'  , d1_sum, end= ' ' )
print( '\n Sum of Diagonal' , d2 , 'is'  , d2_sum, end= ' ' )
