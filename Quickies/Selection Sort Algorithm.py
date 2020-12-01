a = [5,3,8,6,7,2]

for x in range(len(a)):
    minvalue = x
    for y in range(x, len(a)):
        if a[y] < a[minvalue]:
            minvalue = y
    if minvalue != x:
        a[minvalue] , a[x] = a[x] , a[minvalue]
    print(a)
