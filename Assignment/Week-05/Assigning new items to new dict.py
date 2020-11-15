dictionary = {'a' : 6, 'b' : 7, 'c' : 9, 'd' : 8, 'e' : 11}
#assigning new items to new dict
sex = {}
for x,y in dictionary.items():
    if y>=1:
        sex[x] = y
print(sex)
