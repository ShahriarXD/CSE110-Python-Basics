l = a.split(', ')
list = []
for x in range(len(l)):
    list.append(l[x])
list2 = []
for y in list:
    if y not in list2 and y !="," and y!=" ":
        list2.append(y)
list3 = []
for z in list2:
    list3.append(int(z))
print(list3)
