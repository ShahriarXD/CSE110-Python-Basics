# Write Python code of a program to compute and display a person’s weekly salary as determined by the following conditions: If the hours worked are less than or equal to 40, the person receives Tk200.00 per hour, else the person receives Tk8000.00 plus Tk300.00 for each hour worked over 40 hours. The program should request the hours worked as input and should display the salary as output.

# ==========================================================

# hint: You can consider the hour(the user input) to be an integer

# ==========================================================

# Example1:
# Input: 100
# Output: 26000

# ==========================================================

# Example2:
# Input: 30
# Output: 6000


#This code is licensed to Brac University
#Email: km.shahriar.hossain@g.bracu.ac.bd
#Author: KM SHAHRIAR HOSSAIN
#Student Id :20201090


hour = int(input("Enter Your Working Hour: \n"))

if hour <= 40:
    worker_recieves = hour * 200
    print (worker_recieves)

elif hour > 40:
    overtime = hour - 40
    overtime_sallery = overtime *300
    bonus = 8000
    sallery = overtime_sallery + bonus
    print (sallery)
