# Ask the user for a range (a starting number and an ending number). Count how many numbers are prime numbers and how many numbers are perfect numbers between that range and print those numbers.

# =========================================================================

# Hint (1): Declare two strings/lists to store the prime and perfect numbers. Inside the iteration store the values of the prime and perfect numbers in the pre- declared variables.

# Hint (2): Need to use string concat.

# ans = "Prime numbers:"
# prime_value = 11

# ans = ans + str(11)

# print(ans)

# ans = ans + str(13)

# print(ans)

# =========================================================================

# Example:between 2 and 6, there are 3 prime numbers (2, 3, 5) and 1 perfect number (6).

# Input:
# 2

# 6

# Output:
# Between 2 and 6,
# Found 3 prime numbers
# Found 1 perfect number.
# Prime numbers: 2, 3, 5.
# Perfect numbers: 6.


#This code is licensed to Brac University
#Email: km.shahriar.hossain@g.bracu.ac.bd
#Author: KM SHAHRIAR HOSSAIN
#Student Id :20201090
a = int(input())
b = int(input())
count = 0
list = []
sum = 0
count1 = 0
for x in range (a,b+1):
    if x > 1:
        for y in range(2,x):
            if x % y == 0:
                break
        else:
            list.append(x) 
            count += 1		
for lol in range(1 , b-1 , 1):    
    if b % lol == 0:
        sum = sum + lol
if sum == b:
    count1 = count1+1            	
print(f"Between {a} and {b},")
print(f"Found {count} prime numbers")
print(f"Found {count1} perfect number.")
conversion = [str(int) for int in list]
final = ", ".join(conversion)
print(f"Prime numbers: {final}.")
print(f"Perfect numbers: {sum}.") 
