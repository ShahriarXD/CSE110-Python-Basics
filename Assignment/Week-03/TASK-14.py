# Write a Python program that takes a number from the user and prints the divisors of that number and then print how many divisors were there. [The input number has to be an INTEGER]

# ==========================================================

# Example01:

# Input:
# 6

# Output:
# 1, 2, 3, 6
# Total 4 divisors.

# ==========================================================

# Example02:

# Input:
# 121

# Output:
# 1, 11, 121
# Total 3 divisors.


a = int(input(""))
cont = 0
for x in range(1 , a-1):    # eikahne -1 deye last er ta baaad dise
    if a % x == 0:
        print(x , end=", ")
        cont = cont + 1
print(a)  # r eikhane last er ta print korsi
print(f"Total {cont+1} divisors.")
