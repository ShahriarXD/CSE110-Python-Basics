Write a Python code of a program that asks the user to enter ten numbers then display the total and the average of ONLY the odd numbers among those ten numbers.

# ==========================================================

# Example01:

# Input:
# 1

# 2

# 3

# 4

# 5

# 6

# 7

# 8

# 9

# 10

# Output: Total is 25 and Average is 5.0

# Explanation:

# Total is 25 = (1+3+5+7+9) and Average is 25/5 = 5.0

# ==========================================================

# Example02:

# Input:
# -20

# 3

# -5

# 40

# -17

# 9

# 20

# -8

# 99

# -200

# Output:

# Total is 89 and Average is 17.8

# Explanation:

# Total is 89 =(3+(-5)+(-17)+9+99) and Average is 89/5 = 17.8




#This code is licensed to Brac University
#Email: km.shahriar.hossain@g.bracu.ac.bd
#Author: KM SHAHRIAR HOSSAIN
#Student Id :20201090

sum = 0
count=0
for x  in range(10):
    a = int(input())
    if a % 2 != 0:
        sum = sum + a
        count +=1
avg = sum /count       
print(f"Total is {sum} and Average is {avg}")



# list = []
# for x in range (1 ,11):
#     a = int(input())
#     list.append(a)

# sum = 0
# for y in list:
#     if y %2 != 0:
#         sum = sum + y

# avg = sum /5       
# print(f"Total is {sum} and Average is {avg}")       
