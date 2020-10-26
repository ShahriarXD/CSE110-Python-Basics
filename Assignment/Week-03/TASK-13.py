# Write a Python program that takes a number and tells how many digits are in that number.
# [Consider the input number has to be an INTEGER]

# You are not allowed to use len() function

# Example: If the user gives 9876, you should print 4.

# Hint: Keep floor dividing by ten and count how many times this could be divided.

# 9876 floor divide by 10, is 987, count that got 1 digit (total 1)
# 987 floor divide by 10, is 98, count that got 1 digit (total 2)
# 98 floor divide by 10, is 9, count that got 1 digit (total 3)
# 9 floor divide by 10, is 0, count that got 1 digit (total 4)

# Done! (When the number becomes 0 your loop should end.)



#This code is licensed to Brac University
#Email: km.shahriar.hossain@g.bracu.ac.bd
#Author: KM SHAHRIAR HOSSAIN
#Student Id :20201090
num = int(input())
count = 0
while (num != 0):
    num = num // 10 
    count += 1
print(count)
