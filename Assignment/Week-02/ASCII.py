#ASCI VALUE a-z = 97-122
#ASCI VALUE A-Z = 65-90
msg = "abcAA123"
lower = ""
upper = ""
for x in msg:
    if 97<=ord(x)<=122:  #lowecase
        lower += x
    elif 64<=ord(x)<=90:  #uppercase
        upper += x
print(lower)
print(upper)

