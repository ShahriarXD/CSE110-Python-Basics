list_one= [1,7,9,10]
list_two= [2,7,6,5]
n_num = list_one+list_two
n_num.sort()
n = len(n_num) 
n_num.sort() 
print(n_num)
if n % 2 == 0: 
	median1 = n_num[n//2] 
	median2 = n_num[n//2 - 1] 
	median = (median1 + median2)/2
else: 
	median = n_num[n//2] 
print("Median is: " + str(median)) 
