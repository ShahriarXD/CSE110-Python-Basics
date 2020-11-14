a = {'Harry':15, 'Draco':8, 'Nevil':19}
b = {'Ginie':18, 'Luna': 14}
print(a,b)

#{'Harry': 15, 'Draco': 8, 'Nevil': 19} {'Ginie': 18, 'Luna': 14}

a = {'Harry':15, 'Draco':8, 'Nevil':19}
b = {'Ginie':18, 'Luna': 14}
c = a.update(b)
print(a)
print(c)

#{'Harry': 15, 'Draco': 8, 'Nevil': 19, 'Ginie': 18, 'Luna': 14}
#None
