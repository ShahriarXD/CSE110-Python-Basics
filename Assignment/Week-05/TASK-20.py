Input = [(20, 80), (31, 80), (1, 22), (88, 11), (27, 11)] 

Output = {} 
for x, y in Input: 
	if y in Output: 
		Output[y].append((x, y)) 
	else: 
		Output[y] = [(x, y)] 

print(Output) 
