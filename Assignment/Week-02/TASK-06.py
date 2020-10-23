# Write Python code of a program that reads an integer, and prints the integer if it is a multiple of either 2 or 5.

# For example, 2, 4, 5, 6, 8, 10, 12, 14, 15, 16, 18, 20, 22 …

# ==========================================================

# hint(1): use the modulus (%) operator for checking the divisibility

# hint(2): You can consider the number to be an integer

# ==========================================================

# Example01:

# Input:
# 5

# Output:
# 5

# ==========================================================

# Example02:

# Input:
# 10

# Output:
# 10

# ==========================================================

# Example03:

# Input:
# 3

# Output:
# Not a multiple



#This code is licensed to Brac University
#Email: km.shahriar.hossain@g.bracu.ac.bd
#Author: KM SHAHRIAR HOSSAIN
#Student Id :20201090


number_1  = int(input("Please Enter The 1st Number: \n"))

if number_1 % 2 == 0:
    print (number_1)
elif number_1 % 5 == 0:
    print (number_1)
else:
    print ("Not a multiple") 
