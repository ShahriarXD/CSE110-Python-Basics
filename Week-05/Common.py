import ast
dict1 = ast.literal_eval(input())
dict2 = ast.literal_eval(input())
common_pairs = dict()
for x in dict1:
    if (x in dict2 and dict1[x] == dict2[x]):
        common_pairs[x] = dict1[x]
print(common_pairs)
