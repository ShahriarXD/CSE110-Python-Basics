f = open("a.txt","r")
s = open("final.txt" , "w")
d = open("country_filter_A.txt" , "w")
for x in f:
    temp = x.split()
    s.write(temp[1]+"    ====>  Code Executed"+"\n")
    #filtering
    if (temp[1][0]) == "A":
        d.write(temp[1]+"    ====>  Code Executed"+"\n")
s = open("final.txt" , "r")
f.close()
s.close()
d.close()