a = input("")
list = []
for x in range(len(a)):
    list.append(a[x])
x = list
previous_value = None
new_lst = []
for elem in x:
   if elem != previous_value:
       new_lst.append(elem)
       previous_value = elem
for x in new_lst:
    print(x,end="")
    
    
    
    
#Also check:
#ttps://www.pylenin.com/blogs/remove-consecutive-duplicates/



a = "AAABBBBCDDBBECE"
list = []
for x in range(len(a)):
    list.append(a[x])
previous_value = None
new_lst = []
for x in list:
    if x != previous_value:
        previous_value = x
        new_lst.append(x)
for x in new_lst:
    print(x,end="")
