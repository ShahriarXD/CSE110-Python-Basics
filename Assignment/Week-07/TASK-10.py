def xxx(arr): 
	if len(arr) < 2: 
		print("Invalid Input") 
		return
	min_l = 0
	min_r = 1
	min_sum = arr[0] + arr[1] 
	for l in range (0, len(arr) - 1): 
		for r in range (l + 1, len(arr)): 
			sum = arr[l] + arr[r]				 
			if abs(min_sum) > abs(sum):		 
				min_sum = sum
				min_l = l 
				min_r = r
	print("Two pairs which have the smallest sum = ", 
			arr[min_l], "and ", arr[min_r]) 
list_one = [1,-8,4,-7,-20,26,70,-85]
xxx(list_one)
