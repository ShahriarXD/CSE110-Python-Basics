str = input("")
upper, lower, number, = 0, 0, 0
for i in range(len(str)): 
	if str[i].isupper(): 
		upper += 1
	elif str[i].islower(): 
		lower += 1
	elif str[i].isdigit(): 
		number += 1
if number > 1 and upper or lower ==0:
    print ("NUMBER")
elif upper or lower > 1 and number ==0:
    print("WORD")
else:
    print("MIXED")
