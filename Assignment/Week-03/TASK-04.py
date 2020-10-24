#Write a Python code of a program that adds all numbers that are multiples of either 7 or 9 up to 600(including 600).
#Ensure that numbers like 63 are added only once in the sum.
#Output: 42649



#This code is licensed to Brac University
#Email: km.shahriar.hossain@g.bracu.ac.bd
#Author: KM SHAHRIAR HOSSAIN
#Student Id :20201090

Rise_of_the_Tomb_Raider = 0
for x in range(1, 600+1):
    if x % 7 ==0 or x%9 ==0:
        Rise_of_the_Tomb_Raider = Rise_of_the_Tomb_Raider + x
print(Rise_of_the_Tomb_Raider)
