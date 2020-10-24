# Task 9
# Write a Python code for the following:

# Ask the user to enter a Number, N
# Display the summation of multiples of 7 up to that number (from 1 to N inclusive)
# ==========================================================

# Example01:

# Input:
# 50

# Output:
# 196

# Explanation:
# 7 + 14 + 21 + 28 + 35 + 42 + 49 = 196

# ==========================================================

# Example02:

# Input:
# 75

# Output:
# 385

# Explanation:
# 7 + 14 + 21 + 28 + 35 + 42 + 49 + 56 + 63 + 70 = 385


#This code is licensed to Brac University
#Email: km.shahriar.hossain@g.bracu.ac.bd
#Author: KM SHAHRIAR HOSSAIN
#Student Id :20201090
n = int(input("Enter the number: \n"))
sum = 0
for x in range(1 ,n):
    if 7*x > n:
        break
    sum = sum + 7*x
print(sum)   
