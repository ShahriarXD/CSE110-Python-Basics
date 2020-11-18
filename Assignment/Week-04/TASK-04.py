a = input("")
for x in range(len(a)):
    lol = ord(a[x])
    bb = lol+1
    if bb == 123:
        print("a",end="")
    else:
        xx = chr(bb)                 #here chr is the opposite of ord
        print(xx , end="")   
