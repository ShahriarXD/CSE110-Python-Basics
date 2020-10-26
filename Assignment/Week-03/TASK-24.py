# Take five numbers from the user and find the minimum and the average of only the even numbers entered by the user. [If the user enters odd numbers ignore them]

# [CANNOT USE MAX,MIN BUILT-IN FUNCTIONS] [FOR THIS TASK YOU DO NOT NEED TO USE LISTS]

# Assume, the first input is always an even number.

# ============================================================

# Example01: If the user enters 10, 4, -1, -100, and 1.
# Output: “Minimum -100”, “Average is 28.66667”

# Input:
# 10

# 4

# -1

# -100

# 1

# Output:
# Minimum -100
# Average is 28.66667

# Explanation:
# Average calculation: (10+4 + (-100))/3 = -86/3=-28.66667

# ============================================================

# Example02: If the user enters 2, 10, 1, 21, and 3.
# Output: Minimum 2”, “Average is 6.0”

# Input:
# 2

# 10

# 1

# 21

# 3

# Output:
# Minimum 2
# Average is 6.0

# Explanation:
# Average calculation: (2+10)/2 = 12/2= 6


#This code is licensed to Brac University
#Email: km.shahriar.hossain@g.bracu.ac.bd
#Author: KM SHAHRIAR HOSSAIN
#Student Id :20201090
quantity = 5
mn = None
total = 0
for x in range(1, quantity+1):
    inp = int(input())
    if mn is None:
        mn = inp
    if inp < mn:
        mn = inp
    if inp % 2 == 0:
        total = total + inp
    if inp % 2 == 0:
        a = x -1
print('Minimum', mn)
print('Average is', total/a)
