# Write a Python code that will calculate the **value of y if the expression** of y is as follows (n is the input):  

# y = 1^2 - 2^2 +3^2 -4^2 +5^2 .........+ n^2


# ==========================================================

# **Example01:** 

# **Input:**\
# 10

# **Output:**\
# -55

# ==========================================================

# **Example02:** 

# **Input:**\
# 20

# **Output:**\
# -210



#This code is licensed to Brac University
#Email: km.shahriar.hossain@g.bracu.ac.bd
#Author: KM SHAHRIAR HOSSAIN
#Student Id :20201090

n = int(input())
sum = 0
for x in range (n+1):
    if x % 2 == 0:
        sum = sum - x*x

sum1 = 0
for x in range (n+1):
    if x % 2 != 0:
        sum1 = sum1 + x*x


final_answer = sum + sum1
print (final_answer)





# n = int(input("Enter a Number: \n"))
# result = 0
# for i in range(1, n + 1) :
# 	if (i % 2 == 0): 
# 			result = result - pow(i, 2) 


# result1 = 0          
# for i in range(1, n + 1) :
# 	if i % 2 != 0: 
# 	    result1 = result1 + pow(i, 2) 


# final = result + result1

# print(final)

