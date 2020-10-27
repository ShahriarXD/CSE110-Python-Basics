#number = int(input())
binary = bin(number)[2:] #usually extra 0b gets printed so we had to remove that xD.
print(binary)




# Write a python program that converts a Decimal Integer number to a Boolean Number.

# *A decimal can be converted to a binary number by keeping track of the remainders after each division of that number by 2. *

# ================================

# For example, to convert 10 to a binary number, we can follow the following approach

# 10/2 = 5 (Remainder 0)
# 5/2 = 2 (Remainder 1)
# 2/2 = 1 (Remainder 0)
# 1/2 = 0 (Remainder 1)

# Take the remainders from bottom to top, which is, 1010. Binary of 10 is 1010.

# Sample Input
# 10

# Sample Output
# 1010

# ================================

# For example, to convert 13 to a binary number, we can follow the following approach

# 13/2 = 6 (Remainder 1)
# 6/2 = 3 (Remainder 0)
# 3/2 = 1 (Remainder 1)
# 1/2 = 0 (Remainder 1)

# Take the remainders from bottom to top, which is, 1101. Binary of 13 is 1101.

# Sample Input
# 13

# Sample Output
# 1101

num = int(input())
count = 0
list= []
while num != 0:
    a = num % 2
    num = num // 2
    list.append(a)
list.reverse()  
conversion = [str(int) for int in list]
final = "".join(conversion)
print(final)
