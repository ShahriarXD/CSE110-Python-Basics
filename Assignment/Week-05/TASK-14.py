dict =  {'A': [1,2,3], 'b': ['1', '2'], "c": [4, 5, 6, 7]}
ctr = sum(map(len, dict.values()))
print(ctr)
