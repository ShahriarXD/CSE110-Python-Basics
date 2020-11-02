list = []
for x in range(5):
    a = int(input(""))
    list.append(a)
print(f"list: {list}")
max_value = list[ 0 ]
list1 = []
for a in list:
    list1.append(a)
    if a > max_value:
        max_value = a
position = list.index(max_value)
min_value = list1[0]
for b in list1:
    if b < min_value:
        min_value = b
position1 = list1.index(min_value)
print(f"Smallest number {min_value} was found at location {position1}")
print(f"Largest number {max_value} was found at location {position}")
