def summation(anything):
    sum = 1
    for x in range(anything):
        sum = sum * (x+1)
    return sum
print(summation(5))    

#Output
#5

def summation(anything):
    if anything == 1:
        return 1
    else:
        return anything * summation(anything-1)

print(summation(5))   

#Output
#5
