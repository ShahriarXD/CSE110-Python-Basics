f = open("a.txt","r")
dict = {}
for x in f:
    temp= x.split(",")
    name = temp[0].strip()
    goal = int(temp[-1].strip())
    dict[goal] = name
final = sorted(dict , reverse=True)
print(final)
sorted_dict = {}
for y in final:
    name = dict[y]
    sorted_dict[name] = y
print(sorted_dict)
a = open("final_list.txt" ,"w")
for x,y in sorted_dict.items():
    a.write(x+"  "+str(y)+"\n")
f.close()
a.close()