# Write Python code of a program that reads an integer, and prints the integer if it is a multiple of 2 and 5.

# ==========================================================

# For example, 10, 20, 30, 40, 50 …

# hint(1): use the modulus (%) operator for checking the divisibility

# hint(2): You can consider the number to be an integer

# ==========================================================

# Example01:

# Input:
# 5

# Output:
# Not multiple of 2 and 5 both

# ==========================================================

# Example02:

# Input:
# 40

# Output:
# 40

# ==========================================================

# Example02:

# Input:
# 40

# Output:
# 40

#This code is licensed to Brac University
#Email: km.shahriar.hossain@g.bracu.ac.bd
#Author: KM SHAHRIAR HOSSAIN
#Student Id :20201090


number_1  = int(input("Please Enter The 1st Number: \n"))

if number_1 % 2 == 0 and number_1 % 5 ==0:
    print (number_1)
elif number_1 % 5 == 0 :
    print ("Not multiple of 2 and 5 both")
elif number_1 % 2 == 0:
    print ("Not multiple of 2 and 5 both")
else:
    print("Not multiple of 2 and 5 both")
