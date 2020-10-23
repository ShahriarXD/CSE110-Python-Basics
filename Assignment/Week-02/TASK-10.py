# Write Python code of a program that reads an integer, and prints the integer if it is NOT a multiple of 2 OR NOT a multiple of 5.

# For example, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22

# ==========================================================

# hint(1): use the modulus (%) operator for checking the divisibility

# hint(2): You can consider the number to be an integer

# ==========================================================

# Example01:

# Input:
# 3

# Output:
# 3

# ==========================================================

# Example02:

# Input:
# 11

# Output:
# 11

# ==========================================================

# Example03:

# Input:
# 20

# Output:
# No

#This code is licensed to Brac University
#Email: km.shahriar.hossain@g.bracu.ac.bd
#Author: KM SHAHRIAR HOSSAIN
#Student Id :20201090


number_1  = int(input("Please Enter The 1st Number: \n"))

if not number_1 % 2 == 0 or not number_1 % 5 == 0:
    print (number_1)
else:
    print ("No")
