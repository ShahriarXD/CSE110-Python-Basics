a = input("")
list = []
for x in range(len(a)):
    list.append(a[x])
list2 = []
for y in list:
    if y not in list2:
        list2.append(y)
        print(y, end="")
