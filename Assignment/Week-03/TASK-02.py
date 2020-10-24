#Write a Python code for the following:

# 1) Ask the user to enter the name of his favorite car.
# 2) Ask the user to enter a Number

# Display the name of the user’s favorite car, the number of times specified in the second step.

# ==========================================================

# Example 01: If the user enters “Toyota” and 20, your program should print the name “Toyota” twenty times.

# Input:
# Toyota
# 2

# Output:
# Toyota
# Toyota

# ==========================================================

# Example02: If the user enters “Veyron” and 5, your program should print the name “Veyron” five times.

# Input:
# Veyron
# 5

# Output:
# Veyron
# Veyron
# Veyron
# Veyron
# Veyron



#This code is licensed to Brac University
#Email: km.shahriar.hossain@g.bracu.ac.bd
#Author: KM SHAHRIAR HOSSAIN
#Student Id :20201090

name = input("Enter the name of your favorite car: \n")
num = int(input("enter a Number: \n"))

for x in range(1, num+1):
    print(name)
