# Write a python program that prints all the fibonacci number from 0 to N where N will be given.

# A Fibonacci number is a number which is the summation of its previous two fibonacci number.

# First two fibonacci number are 0 and 1. So the 3rd Fib will be 0+1=1, 4th Fib will be 1+1=2, 5th Fib will be 1+2=3 and so on.

# ==============================

# Sample Input
# 10

# Sample Output
# 0 1 1 2 3 5 8

# ==============================

# Sample Input
# 15

# Sample Output
# 0 1 1 2 3 5 8 13


#This code is licensed to Brac University
#Email: km.shahriar.hossain@g.bracu.ac.bd
#Author: KM SHAHRIAR HOSSAIN                              
#Student Id :20201090
num = int(input())
a = -1  
b = 1
for x in range(1,num+1): 
    next_number = a+b
    if next_number > num:
        break                               
    print(next_number,end=" ")
    a=b
    b=next_number
