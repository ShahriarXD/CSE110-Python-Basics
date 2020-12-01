a = [-2,312,131,1,15,-99,1,11,5,15,12,1]
print(a)
b = sorted(a)
print(b)
c = sorted(a, reverse=True)
print(c)






[-2, 312, 131, 1, 15, -99, 1, 11, 5, 15, 12, 1]
[-99, -2, 1, 1, 1, 5, 11, 12, 15, 15, 131, 312]
[312, 131, 15, 15, 12, 11, 5, 1, 1, 1, -2, -99]











inventory = {
    "Chips": 10,
    "Mr Twist": 55,
    "Alloz" : 66,
    "Layz" : 55
}
final = sorted(inventory)
print(final)
dict = {}
for x in final:
    dict[x] = inventory[x]
print(dict)
