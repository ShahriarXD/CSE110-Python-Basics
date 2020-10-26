# Write a Python program that takes a number and tells if it is a perfect number or not. [The input number has to be an INTEGER]

# Perfect Number: An integer number is said to be a perfect number if its factors, including 1 but not the number itself, sum to the number.

# ==========================================================

# Example01:

# Input:
# 6

# Output:
# 6 is a perfect number

# Explanation:
# 6 have 4 divisors: 1, 2, 3, and 6.
# If we add all factors except itself, 6 = 1 + 2 + 3.

# ==========================================================

# Example02:

# Input:
# 20

# Output:
# 28 is a perfect number

# Explanation:
# 28 have 6 divisors: 1, 2, 4, 7, 14, and 28.
# If we add all factors except itself, 28 = 1 + 2 + 4 + 7 + 14.

# ==========================================================

# Example03:

# Input:
# 33

# Output:
# 33 is not a perfect number

# Explanation:
# 33 have 3 divisors: 1, 3, 11, and 33.
# If we add all factors except itself, 15 = 1 + 3 + 11.


#This code is licensed to Brac University
#Email: km.shahriar.hossain@g.bracu.ac.bd
#Author: KM SHAHRIAR HOSSAIN
#Student Id :20201090
a = int(input(""))
sum = 0
for x in range(1 , a-1):    
    if a % x == 0:
        sum = sum + x
if sum == a:
    print(f"{sum} is a perfect number")
else:
    print(f"{a} is not a perfect number") 
