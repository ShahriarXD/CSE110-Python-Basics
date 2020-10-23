# Write Python code of a program that reads a student’s mark for a single subject, and prints out the corresponding grade for that mark. The mark ranges and corresponding grades are shown in the table below. You need to make sure that the marks are valid. For example, a student cannot receive -5 or 110. So the valid marks range is 0 to 100.

# hint(1): You can consider the number to be an integer

# hint(2): This problem can be solved in two ways: top-down (starts from A) and bottom-up (starts from F)

# Marks	Grage
# 90 or above	A
# 80-89	B
# 70-79	C
# 60-69	D
# 50-59	E
# Below 50	F



#This code is licensed to Brac University
#Email: km.shahriar.hossain@g.bracu.ac.bd
#Author: KM SHAHRIAR HOSSAIN
#Student Id :20201090


marks = int(input("Enter Your Marks: \n"))

if marks < 0 or marks > 100:
    print (f"Your Mark is  (NOT VALID) ")
elif marks>=90:
    print  ("A")    
elif marks>=80:
    print  ("B")
elif marks>=70:
    print  ("C")
elif marks>=60:
    print  ("D")
elif marks>=50:
    print ("E")
else:
    print ("F")
