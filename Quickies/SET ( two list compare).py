list_one = [1, 2 , 3, 2, 4, 5, 5, 7, 99, 200, 303, 70]
list_two = [1, 1, 2, 3, 3, 3, 4, 5, 200, 500, -5]

final_list = list(set(list_one) | set(list_two))
print(final_list)

