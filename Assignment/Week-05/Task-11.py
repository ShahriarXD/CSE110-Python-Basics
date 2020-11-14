dict1 = {'a': 10, 'b':20, 'c':30}
dict2 = {'a': 10, 'c':20, 'd':30, 'e':40}
for x ,y in dict2.items():
    if x in dict1.keys():
        dict1[x] += y
    else:
        dict1[x] = y
print(dict1)

# import ast
# dict1 = ast.literal_eval(input())
# dict2 = ast.literal_eval(input())
# final_dictionary = {x: dict1.get(x, 0) + dict2.get(x, 0) for x in set(dict1).union(dict2)} 
# print(final_dictionary)
