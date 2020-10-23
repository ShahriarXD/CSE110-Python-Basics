# Write Python code of a program that reads a number, and prints "The number is even" or "The number is odd", depending on whether the number is even or odd.

# hint(1): use the modulus (%) operator

# hint(2): You can consider the number to be an integer

# ==========================================================

# Example:

# Input:
# 5

# Output:
# The number is odd

# ==========================================================

# Example:

# Input:
# -44

# Output:
# The number is even

#This code is licensed to Brac University
#Email: km.shahriar.hossain@g.bracu.ac.bd
#Author: KM SHAHRIAR HOSSAIN
#Student Id :20201090




number_1  = int(input("Please Enter The 1st Number: \n"))

if number_1 % 2 == 0:
    print ("The number is even")
else:
    print ("The number is odd") 
