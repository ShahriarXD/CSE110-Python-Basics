from collections import Counter 
dict1 = Counter({'a': 10, 'b':20, 'c':30})
dict2 = Counter({'a': 10, 'c':20, 'd':30, 'e':40})

final_dictionary = dict1  + dict2 
print (final_dictionary) 

dict1 = {'a': 10, 'b':20, 'c':30}
dict2 = {'a': 10, 'c':20, 'd':30, 'e':40}


# combining dictionaries 
# using dict comprehension and set 
final_dictionary = {x: dict1.get(x, 0) + dict2.get(x, 0) 
					for x in set(dict1).union(dict2)} 

# printing final result 
print (final_dictionary)
