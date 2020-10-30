number = [1,2,3,4,5,6,7,8,9,10]
list= []
for x in number:
    a = x*x
    list.append(a)
print (list) 




#alternate





number = [ 1,2,3,4,5,6,7,8,9,10 ]
def square(number):
    a = number*number
    return a
result = list(map(square,number))
print(result)
