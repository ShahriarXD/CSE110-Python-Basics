ints = [1,2,3]
string_ints = [str(int) for int in ints]
#Convert each integer to a string


str_of_ints = ",".join(string_ints)
#Combine each string with a comma


print(str_of_ints)
