a = "12345"
c = a[2::-1]
list = []
for x in range(len(a)+1):
    list.append(a[3:x])
a = list[-1]
print(f"{c}{a}")
