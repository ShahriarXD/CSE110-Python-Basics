#map and #filter function workd with list. where xxxargs works with dict.


#MAP
# map(func,iter)
# jodi list dewa thake taile amra map fuction use korbo

number = [ 1,2,3,4,5,6,7,8,9,10 ]

def square(number):
    a = number*number
    return a

result = list(map(square,number))
print(result)
