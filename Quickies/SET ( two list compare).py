list_one = [1, 2 , 3, 2, 4, 5, 5, 7, 99, 200, 303, 70]
list_two = [1, 1, 2, 3, 3, 3, 4, 5, 200, 500, -5]

final_list = set(list_one) | set(list_two)
print(final_list)

final_list = set(list_one) and set(list_two)  
print(final_list)


final_list = set(list_two) and set(list_one)  
print(final_list)

list_one = [1, 2 , 3, 2, 4, 5, 5, 7, 99, 200, 303, 70]
list_two = [1, 1, 2, 3, 3, 3, 4, 5, 200, 500, -5]
final_list = list(set(list_one) | set(list_two))
print(final_list)





"""
{1, 2, 3, 4, 5, 99, 7, 200, 70, 303, 500, -5}
{1, 2, 3, 4, 5, 200, 500, -5}       
{1, 2, 3, 4, 5, 99, 7, 200, 70, 303}
[1, 2, 3, 4, 5, 99, 7, 200, 70, 303, 500, -5]
"""
