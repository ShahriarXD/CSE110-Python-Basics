a = input("")
sting1 = ""
for x in a:
    if x != " ":
        sting1 += x
dict = {}
for y in sting1.lower():
    if y in dict:
        dict[y] += 1
    else:
        dict[y] = 1
print(dict) 
