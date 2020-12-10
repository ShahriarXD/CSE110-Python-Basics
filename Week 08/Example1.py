f = open("a.txt", "w")
f.write("Bangladesh\n")
f.write("Bangladesh\n")
f.write("Bangladesh\n")
f.write("Bangladesh\n")
f = open("a.txt", "r")
for x in f:
    a = x.split()
    print(a)
    
    
    
    
    
    
['Bangladesh']
['Bangladesh']
['Bangladesh']
['Bangladesh']
