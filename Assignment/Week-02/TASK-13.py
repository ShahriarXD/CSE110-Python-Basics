# Write Python code of a program that finds the number of hours, minutes, and seconds in a given number of seconds.

# ==========================================================

# hint(1): The user input will be an integer value

# hint(2): 1 hour = 60 mins = 3600 seconds
# 1min = 60 seconds

# ==========================================================

# Example01:
# Input: 10000
# Output: Hours: 2 Minutes: 46 Seconds: 40

# ==========================================================

# Example02:
# Input: 500
# Output: Hours: 0 Minutes: 8 Seconds: 20

sec = int(input("Enter the Value in seconds to get result: \n"))

minute = sec / 60
a = int(minute)

if a >= 60:
    hour = a /60
    b = int(hour)
    minute1 = minute - (b * 60)
    d = int(minute1)
    sec1 = sec - (a * 60)
    print (f"Hours: {b} Minutes: {d} Seconds: {sec1}")
elif a < 60:
    sec1 = sec - (a * 60)   
    print (f"Hours: 0 Minutes: {a} Seconds: {sec1}")
