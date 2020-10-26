# Write a Python program that asks the user for one number and tells if it is a prime number or not. [The input number has to be an INTEGER]

# Prime Number: If a number has only two divisors, (1 and itself), then it is prime. If it is divisible by more numbers, then it is not a prime.

# ==========================================================

# Hint: use the divisor count from task 16.

# ==========================================================

# Example01:

# Input:
# 11

# Output:
# 11 is a prime number

# Explanation:
# 11 has only 2 divisors: 1, and 11.

# ==========================================================

# Example02:

# Input:
# 6

# Output:
# 6 is not a prime number

# Explanation:
# 6 have 4 divisors: 1, 2, 3 and 6.


#This code is licensed to Brac University
#Email: km.shahriar.hossain@g.bracu.ac.bd
#Author: KM SHAHRIAR HOSSAIN
#Student Id :20201090
number = int(input())
if number > 1:
   for x in range(2,number):
       if number % x == 0:
           print(number,"is not a prime number")
           break
   else:
       print(number,"is a prime number")
else:
   print(number,"is not a prime number")
