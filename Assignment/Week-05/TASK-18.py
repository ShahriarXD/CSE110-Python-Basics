my_dictionary = {'c1': 'Red', 'c2': 'Green', 'c3': None, 'd4': 'Blue'}
dict = {}
for x,y in my_dictionary.items():
    if y is not None:
        dict[x] = y
print(dict)


# Easy in one line using list comprehension Method
#my_dictionary = {'c1': 'Red', 'c2': 'Green', 'c3': None, 'd4': 'Blue'}
#print({k:v for k, v in my_dictionary.items() if v is not None})
