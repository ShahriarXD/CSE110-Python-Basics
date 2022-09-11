# In set it does not print any types of duplicate value.


import numbers


name = {1,2,3,3,4,3,3,5}
print(name)

# Converting List into a set.
name1 = [0,1,1,1,2,1,3]
name2 = set(name1)
print(name2)
# Adding value in set is add() we know in list its append
# when we add and pop here remove() when we remove
name2.add("KIk")
print(name2)
name2.remove("KIk")
print(name2)


# Now we are going to learn about union.

number1 = {1,2,3,4,5,5,5,5,5,5,4,5,6}
number2 = {1,2,3,3,7,2,2,8,9,10}
# So To use union we use this |
print(number1 | number2)
# So To use Intercetion we use this & ( It only prints the common section)
print(number1 & number2)
# And minus to differentiate. Name set 2 te ja ase oita baad deye only set 1 print hobe
print(number1 - number2)
