#taking int he number of scores to be submitted
num=int(input( " Please enter the number of scores considered for comparison : "))
# taking usser input and storing in lists
alice=[int(c) for c in input("Please Enter Alice's scores seprated by space : ").split()]
bob=[int(c) for c in input("Please Enter Bob's Scores separated by space : ").split()]
#comapring for bigger number in both lits
compare=['a1' for i in range(num) if alice[i]>bob[i]]
#print(compare)
compare+=['b1' for i in range(num) if alice[i]<bob[i]]
#print(compare)
#counting the points for alice and bob and printing the same.
alice_point=compare.count('a1')
bob_points=compare.count('b1')
print ('Alice Earned a total of ', alice_point ' points ')
print (' Bob Earned a total of ' , bob_points , 'points ')
