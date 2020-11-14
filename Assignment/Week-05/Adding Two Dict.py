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




a = {'Harry':15, 'Draco':8, 'Nevil':19}
b = {'Ginie':18, 'Luna': 14}
c = a.copy()
print(c)
#{'Harry': 15, 'Draco': 8, 'Nevil': 19}


a = {'Harry':15, 'Draco':8, 'Nevil':19}
b = {'Ginie':18, 'Luna': 14}
print(a | b)
#{'Harry': 15, 'Draco': 8, 'Nevil': 19, 'Ginie': 18, 'Luna': 14}



def add(dict1, dict2):
    result = {**dict1, **dict2}
    return result
dict1 = {'Harry':15, 'Draco':8, 'Nevil':19}
dict2 = {'Ginie':18, 'Luna': 14}
print(add(dict1,dict2))
#{'Harry': 15, 'Draco': 8, 'Nevil': 19, 'Ginie': 18, 'Luna': 14}
