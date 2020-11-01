list = []
for x in range(5):
    a = int(input(""))
    list.append(a)
print(f"list: {list}")
max_value = list[ 0 ]
for a in list:
    if a > max_value:
        max_value = a
position = list.index(max_value)
print(f"Largest number {max_value} was found at location {position}.")



# list = []
# for x in range(5):
#     a = int(input(""))
#     list.append(a)
# print(list)
# list.sort()
# a = list[-1]
