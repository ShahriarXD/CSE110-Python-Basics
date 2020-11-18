list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = [x for x in list_one if x%2 ==0]

list_two = [10, 11, 12, -13, -14, -15, -16]
b = [x for x in list_two if x%2 ==0]


a.extend(b)
list_final = []          #with a new list
list_final.extend(a) 
print(list_final)




list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gg = []
for x in list_one:
    if x%2 ==0:
        gg.append(x)
list_two = [10, 11, 12, -13, -14, -15, -16]
ns = []
for x in list_two:
    if x%2 ==0:
        ns.append(x)
gg.extend(ns)
list_final = []          #with a new list
list_final.extend(gg) 
print(list_final)
