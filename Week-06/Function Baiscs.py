def anythinghh(lol):
    return lol
print(anythinghh("xxx"))


def numeb(x,a,b):
    sum = x+a
    return sum
print(numeb(55,5,500000000))




def number(*anything):
    print(anything[1])
number("" , 101 ,555)    



def number1(*anything):
    sum = 0
    for x in anything:
        sum += x
    return sum
print(number1(55, 101 , 1111))
