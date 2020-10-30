#LAMBDA FUNCTION
# HOW TO WRITE:
#LAMBDA PARAMETER : EXPRESSION , (value)
#(lambda x,n : x** + 2*xn + n** (value) )
NOOB = (lambda x,n : x*x + 2*x*n + n*n) (2,3)
print (NOOB)
Sexy = (lambda maal: maal*maal + 55) (5)
print (Sexy)



#MAP FUNCTION
def sq(x):
    a = x*x
    return a
number = [1 , 2 , 4, 3, 5]
xnxx = list(map(sq , number))
print (xnxx)


#FILTER FUNCTION 

list1 = [ 55 ,66 ,88 , 5555]

RESULT = list(filter(lambda F: F%2 == 0,list1))
print(RESULT)


#===========================OUTPUT================================
#25
#80
#[1, 4, 16, 9, 25]
#[66, 88]
