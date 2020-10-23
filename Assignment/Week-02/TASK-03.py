## Write Python code of a program that reads two numbers from the user. 
# Your program should then print "First is greater" if the first number is greater, 
# "Second is greater" if the second number is greater, and "The numbers are equal" otherwise.

# ==========================================================

# Example:

# Input:
# -4
# -4

# Output:
# The numbers are equal

# ==========================================================

# Example:

# Input:
# -40
# -4

# Output:
# Second is greater

# ==========================================================

# hint: You can consider the numbers to be floating point values



#This code is licensed to Brac University
#Email: km.shahriar.hossain@g.bracu.ac.bd
#Author: KM SHAHRIAR HOSSAIN
#Student Id :20201090


number_1  = float(input("Please Enter The 1st Number: \n"))
number_2  = float(input("Please Enter The 2nd Number: \n"))


if number_1 > number_2:
    print ("First is greater")
elif number_2 > number_1:
    print ("Second is greater")    
elif number_1 == number_2:
    print ("The numbers are equal")  
