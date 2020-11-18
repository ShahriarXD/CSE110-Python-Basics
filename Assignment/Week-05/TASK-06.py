aa = ('a','b','c','d','e','f','g','h')
bb = reversed(aa)
print(tuple(bb))


#METHOD 1
#aa = ('a','b','c','d','e','f','g','h')
#bb = aa[::-1]
#print(bb)


#METHOD 2
# import ast
# a = ast.literal_eval(input())
# bb = a[::-1]
# print(bb)


#METHOD 3
# Number_of_Item_you_want = int(input())
# list = []
# for x in range(Number_of_Item_you_want):
#     a = input("")
#     list.append(a)
# b = tuple(list)
# bb = reversed(b)
# print(tuple(bb))

#METHOD 4
aa = ('a','b','c','d','e','f','g','h')
# list= []
# for x in aa:
#     list.append(x)
# aa = list[::-1]
# print(tuple(aa))

