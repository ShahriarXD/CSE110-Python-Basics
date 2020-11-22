a = input("")
b = input("")
for x in range(len(a)):
    if x % 2 == 0:
        print(a[x],end="")
    else:
        print(b,end="")
