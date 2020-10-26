# Write a python program that prints a right angled triangle of height N using incrementing numbers where N will be given as input.

# ====================================

# Sample Input 4

# Sample Output
# 1
# 12
# 123
# 1234

# ====================================

# Sample Input 5

# Sample Output
# 1
# 12
# 123
# 1234
# 12345

#This code is licensed to Brac University
#Email: km.shahriar.hossain@g.bracu.ac.bd
#Author: KM SHAHRIAR HOSSAIN
#Student Id :20201090
n = int(input())
for x in range(1, n+1):
    for y in range(1 , x+1):
        print(y, end="")
    print()
