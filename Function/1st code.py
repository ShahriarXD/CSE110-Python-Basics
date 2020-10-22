def a(dd):
    print ("hello ", dd) 

a("Mahir") 
a("Rohim") 





def a(a,b):
    sum = a+b
    print (sum)

a(5,6) 
a(5,116) 





def b(*trmairechudi):
    sum = 0
    for x in trmairechudi:
        sum = sum +x
    print(sum)

b(5,6)    
b(5,6,11,55)


def a(*dd):
    print (f"Hello {dd[0]} and {dd[1]}") 

a("Mahir" , "NAFISA") 
a("Rohim" , "SAMIA") 
