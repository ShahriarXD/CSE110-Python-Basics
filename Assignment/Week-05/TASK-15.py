list_1 = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]
dict = {}
for x in list_1:
    if x[0] not in dict:
        dict[x[0]] = [x[1]]   #here we are converting it into list
    else:
        dict[x[0]].append(x[1])  #we can append a list
print(dict)



# list_1 = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]
# dict_1=dict() 
# for x,y in list_1: 
# 	dict_1.setdefault(x, []).append(y) 
# print(dict_1) 
