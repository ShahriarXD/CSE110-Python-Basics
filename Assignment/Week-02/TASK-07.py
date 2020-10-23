# Write Python code of a program that reads an integer, and prints the integer it is a multiple of either 2 or 5 but not both.

# For example, 2, 4, 5, 6, 8, 12, 14, 15, 16, 18, 22 …

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
# multiple of 2 and 5 both

# ==========================================================

# Example02:

# Input:
# 44

# Output:
# 44

#This code is licensed to Brac University
#Email: km.shahriar.hossain@g.bracu.ac.bd
#Author: KM SHAHRIAR HOSSAIN
#Student Id :20201090


number_1  = int(input("Please Enter The 1st Number: \n"))

if number_1 % 2 == 0 and number_1 % 5 ==0:
    print ("multiple of 2 and 5 both")
elif number_1 % 5 == 0 :
    print (number_1)
elif number_1 % 2 == 0:
    print (number_1)
