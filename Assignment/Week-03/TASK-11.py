# Write a Python program which takes a number and prints the digits from the unit place, then the tenth, then hundredth, etc. (Right to Left)

# [Consider the input number to be an INTEGER]

# Example: If the user gives 32768, then print 8, 6, 7, 2, 3

# =========================================================================

# Hint: The input() function, converts the input data to String data type by default. Use this knowledge to solve this problem.



n = input()[::-1]
a = len(n)
for x in range(0 , a-1):
    print(n[x], end=", ")
else:
    print(n[x+1])   
