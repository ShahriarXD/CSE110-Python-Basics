# Write a python program that prints a rectangle of size M (height/line numbers) and N(length/column numbers) using incrementing numbers where M,N will be given as input.

# ===================================

# Sample Input 4,6

# Sample Output
# 123456
# 123456
# 123456
# 123456

# ===================================

# Sample Input 3,2

# Sample Output
# 12
# 12
# 12


#This code is licensed to Brac University
#Email: km.shahriar.hossain@g.bracu.ac.bd
#Author: KM SHAHRIAR HOSSAIN
#Student Id :20201090
a = int(input())
b = int(input())
for x in range(1, a+1):
    for y in range(1, b+1):
        print(y , end="")
    print()    
