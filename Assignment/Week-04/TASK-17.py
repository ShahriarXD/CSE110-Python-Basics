a = input("")
for x in range(len(a)):
    if x % 2 == 0:
        print(a[x].upper(), end ="")
    elif x % 2 != 0:
        print(a[x].lower(), end ="")
