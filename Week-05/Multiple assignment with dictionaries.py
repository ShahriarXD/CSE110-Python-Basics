d = {'a':10, 'b':1, 'c':22}
for key, val in d.items():
    print(val,key)

d = {'a':10, 'b':1, 'c':22}
l = list()
for key, val in d.items():
    l.append( (key,val) )
print(l)
l.sort(reverse=True)
print(l)





# 10 a
# 1 b
# 22 c
# [('a', 10), ('b', 1), ('c', 22)]
# [('c', 22), ('b', 1), ('a', 10)]
