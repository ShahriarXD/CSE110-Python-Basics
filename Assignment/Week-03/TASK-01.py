# Write python program, which prints the following sequences of values in loops:

# a) 24, 18, 12, 6, 0, -6
# b) -10, -5, 0, 5, 10, 15, 20
# c) 18, 27, 36, 45, 54, 63
# d) 18,-27, 36,-45,54,-63

# =====================================================================

# Hints(1): Use a while loop for solving these problems.

# Hints(2): We are already familiar with the print() function. But when we use it to print any value it automatically adds an additional newline after each print statement.

# For example:
# print(1)
# print(2)

# Output:
# 1
# 2

# =====================================================================

# To solve this problem, in Python3, we need to add an extra argument (end = " ") in the print function which tells the program to skip printing the additional newline.

# For example:
# print(1, end =" ")
# print(2)

# Output:(prints the next output right to the previous one)
# 12

# =====================================================================

# In Task-1(a), the loop counter should be initialized at 24 and the loop should terminate when the loop counter reaches -6. The difference between the first two values is 24-18=6. So the loop counter value is getting decremented by 6 in every iteration.

# For your understanding task 1(a) code is done for you.
# b)-10, -5, 0, 5, 10, 15, 20
#This code is licensed to Brac University
#Email: km.shahriar.hossain@g.bracu.ac.bd
#Author: KM SHAHRIAR HOSSAIN
#Student Id :20201090






count = -10
while count <= 20:
    print(count , end =", ")
    count += 5
