# Write a Python program that asks the user for a quantity then takes that many numbers and prints the maximum, minimum and average of those numbers.

# [CANNOT USE MAX,MIN BUILT-IN FUNCTIONS][FOR THIS TASK YOU DO NOT NEED TO USE LISTS]

# ==========================================================

# Example01: If the user enters 5 as an input for quantity. Then enters 10, 4, -1, -100, and 1.
# Your program output should be: “Maximum 10”, “Minimum -100”, “Average is -17.2”

# Input:
# 5 10 4 -1 -100 1.

# Output:
# Maximum 10
# Minimum -100
# Average is -17.2

# Explanation:
# Average calculation: (10+4 + (-1) + (-100) + 1)/5 = -86/5=-17.2

#This code is licensed to Brac University
#Email: km.shahriar.hossain@g.bracu.ac.bd
#Author: KM SHAHRIAR HOSSAIN
#Student Id :20201090


a = int(input())
maxium = None
minimum =None
sum = 0
for x in range(a):
    b = int(input())
    sum = sum + b
    if maxium is None and minimum is None:
        maxium = b
        minimum = b
    elif b > maxium:
        maxium = b
    elif b < minimum:
        minimum = b
avg = sum/a
print('Maximum',maxium)
print('Minimum',minimum)
print('Average is',avg)








# quantity = int(input())
# mx = None
# mn = None
# total = 0
# for i in range(quantity):
#     inp = int(input())
#     total = (inp + total)
#     if mn is None and mx is None:
#         mn = inp
#         mx = inp
#     elif inp < mn:
#         mn = inp
#     elif inp > mx:
#         mx = inp
# avg = total/quantity        
# print('Maximum',mx)
# print('Minimum',mn)
# print('Average is',avg)
