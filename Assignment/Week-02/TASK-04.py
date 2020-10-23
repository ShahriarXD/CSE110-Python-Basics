# Write Python code of a program that reads two numbers, subtracts the smaller number from the larger one, and prints the result.

# hint(1): First check which number is greater

# hint(2): You can consider the numbers to be floating point values

# ==========================================================

# Example:

# Input:
# -40
# -4

# Output:
# 36

# ==========================================================

# Example:

# Input:
# 6
# 2

# Output:
# 4

#This code is licensed to Brac University
#Email: km.shahriar.hossain@g.bracu.ac.bd
#Author: KM SHAHRIAR HOSSAIN
#Student Id :20201090


number_1  = int(input("Please Enter The 1st Number: \n"))
number_2  = int(input("Please Enter The 2nd Number: \n"))


if number_1 > number_2:
    sub = number_1 - number_2
    print(sub)
elif number_2 > number_1:
    sub = number_2 - number_1
    print(sub)  
