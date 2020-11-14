a = input("").split(", ")[:-1]
list=[]
for x in a:
    if x not in list:
        list.append(x)
        count=0
        for y in range(len(a)):
            if a[y] == x:
                count+=1
        print(f"{x} - {count} times")
