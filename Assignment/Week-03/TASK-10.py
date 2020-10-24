# Write a Python code that will read 10 numbers from the user, and then print the first number, the sum of the first 2 numbers, the sum of the first 3 numbers, and so on up to the sum of 10 numbers.

# ==========================================================

# For example,

# The user enters 10, output 10, then
# The user enters 2, (10+2) = 12, output 12, then
# The user enters 4, (10+2+4) = 16, output 16, then
# The user enters 20, (10+2+4+20) = 36, output 36, and continuous till the 10 th  input


#This code is licensed to Brac University
#Email: km.shahriar.hossain@g.bracu.ac.bd
#Author: KM SHAHRIAR HOSSAIN
#Student Id :20201090
GTA5 = 0
for i in range(1 ,11):
    usr_input = int(input())
    GTA5 = GTA5 + usr_input
    print(f"OUTPUT {GTA5}")
