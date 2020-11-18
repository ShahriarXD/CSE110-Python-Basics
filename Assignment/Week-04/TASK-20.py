
list_one = [1, 2 , 3, 2, 4, 5, 5, 7, 99, 200, 303, 70]
list_two = [1, 1, 2, 3, 3, 3, 4, 5, 200, 500, -5]
list_four = []
for y in list_two:
    if y not in list_one:
        list_four.append(y)
fun = set(list_one) and set(list_one)
list_three = []
for x in fun:
    list_three.append(x)
list_final = list_three + list_four
print(list_final)

# Easy Version xD
# list_one = [1, 2 , 3, 2, 4, 5, 5, 7, 99, 200, 303, 70]
# list_two = [1, 1, 2, 3, 3, 3, 4, 5, 200, 500, -5]
# final_list = list(set(list_one) | set(list_two))
# print(final_list)
