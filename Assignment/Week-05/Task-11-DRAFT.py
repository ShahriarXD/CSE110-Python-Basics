from collections import Counter 
dict1 = Counter({'a': 10, 'b':20, 'c':30})
dict2 = Counter({'a': 10, 'c':20, 'd':30, 'e':40})

final_dictionary = dict1  + dict2 
print (final_dictionary) 

