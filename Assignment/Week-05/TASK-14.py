dict =  {'A': [1,2,3], 'b': ['1', '2'], "c": [4, 5, 6, 7]}
ctr = sum(map(len, dict.values()))
print(ctr)



dict = {'A': [1,2,3], 'b': ['1', '2'], "c": [4, 5, 6, 7]}
count = 0
for x , y in dict.items():
    for z,a in dict.items():
        count += 1
print(count)        




dict = {'A': [1,2,3], 'b': ['1', '2'], "c": [4, 5, 6, 7]}
count = 0
for x in dict:
    ff = dict[x]
    for y in ff:
        count += 1
print(count)
