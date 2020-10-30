#xxargs will work as tupple

def summation(*ab):
    return ab
print(summation(55,55,66))
print(summation(55,66,55))
print(summation(54,66,55,5,5,5,5,5,5)) 
#OUTPUT
#(55, 55, 66)
#(55, 66, 55)
#(54, 66, 55, 5, 5, 5, 5, 5, 5)




#Using Index

def summation(*ab):
    return ab[2]
print(summation(55,55,66))
print(summation(55,66,55))
print(summation(54,66,55,5,5,5,5,5,5)) 
#OUTPUT
#66
#55
#55



#=================================================================================


def summation(*anything):
    sum = 0
    for x in anything:
        sum = sum + x
    return sum
print(summation(55,55,66))
print(summation(55,66,55))
print(summation(54,66,55,5,5,5,5,5,5))  

#OUTPUT 
#176
#176
#205
