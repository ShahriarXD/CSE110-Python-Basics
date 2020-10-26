# Write a Python code for the following:

# Ask the user to enter a number, N (Total number of inputs to be taken). Assume that the user will never enter the first number as zero.
# Take N number of inputs
# Prints out the product of all the numbers read
# For example, if the first input is 4, then the program has to read in four numbers from the user and print the product of these four numbers.

# =========================================================================

# Example01:

# Input:
# 5

# 10

# 6

# 4

# 2

# 1

# Output:
# 480

# Explanation:
# 5 is the total number of inputs taken. Then, the calculation should be 10 X 6 X 4 X 2 X 1 = 480

#This code is licensed to Brac University
#Email: km.shahriar.hossain@g.bracu.ac.bd
#Author: KM SHAHRIAR HOSSAIN
#Student Id :20201090
num = int(input())
gun = 1
for x in range(1 ,num+1):
    a = int(input())
    gun = gun * a
print(gun) 
