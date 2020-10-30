def amr_function(number1 , number2, number3):
    if number1>number2:
        if number1>number3:
            return number1
        else:
            return number2
    elif number2>number3:
        return number2
    else:
        return number3

a = amr_function(100,55,60)        
print(a)
