# Suppose the following expressions are used to calculate the values of L for different values of S:

# L=3000−125S2  if  S<100 

# L=120004+S2/14900  if  S≥100 

# Write a Python code of a program that reads a value of S and then calculates the value of L.

# ==========================================================

# hint(1): You can import math and use math function for making squares math.pow(number, power) Or you can simply write S**2.

# hint(2): The value of S(user input) will be an integer

# ==========================================================

# Example01:
# Input: 120
# Output: 2416.2162162162163

# ==========================================================

# Example02:
# Input: 3
# Output: 1875

value_of_s = int(input("Enter The Value of S: \n"))
if value_of_s < 100:
    L = 3000 - (125 * value_of_s ** 2)
    print (L) 
elif value_of_s >= 100:
    L = 12000/(4+value_of_s**2/14900)
    print (L)
