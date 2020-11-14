my_dictionary = {'c1': 'Red', 'c2': 'Green', 'c3': None, 'd4': 'Blue'}
print({k: v for k, v in my_dictionary.items() if v is not None})
