a = input()
b = a.split(", ")
list = []
for x in b:
    list.append(x)

c = input()
d = c.split(", ")
list1 = []
for y in d:
    list1.append(y)


list3 = []
for z in list:
    if z in list1:
        list3.append(z)
print(list3)
