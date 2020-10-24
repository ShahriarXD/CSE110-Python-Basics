#Write a Python code of a program that adds all numbers that are multiples of either 7 or 9 but not both, up to 600(including 600).
#Output: 39814

#This code is licensed to Brac University
#Email: km.shahriar.hossain@g.bracu.ac.bd
#Author: KM SHAHRIAR HOSSAIN
#Student Id :20201090


MSI = 0
for x in range(0, 600+1):
    if x % 7 ==0 or x%9 ==0:
        if not (x % 7 ==0 and x%9 ==0):
            MSI = MSI + x
print(MSI)
