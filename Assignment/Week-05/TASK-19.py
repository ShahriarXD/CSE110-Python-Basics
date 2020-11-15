dictionary = {'a' : 6, 'b' : 7, 'c' : 9, 'd' : 8, 'e' : 11}
a = int(input())
b = int(input())
dict = {}
for x , y in dictionary.items():
    if(y>=a and y<=b):
        dict[x] = y 
print(dict)
