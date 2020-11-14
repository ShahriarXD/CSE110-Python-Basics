a = {'Harry':15, 'Draco':8, 'Nevil':19}
b = {'Ginie':18, 'Luna': 14}
c = a.copy()
c.update(b)
print(c)

#METHOD 1
# a = {'Harry':15, 'Draco':8, 'Nevil':19}
# b = {'Ginie':18, 'Luna': 14}
# c = a.copy()
# print(c | b)


#METHOD 2
# def add(a, b):
#     result = {**a, **b}
#     return result
# a = {'Harry':15, 'Draco':8, 'Nevil':19}
# b = {'Ginie':18, 'Luna': 14}
# print(add(a,b))
