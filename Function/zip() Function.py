#The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
#If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.



#ZIP FUNCTION
#zip(list1 , list2)
#and we need to knoww that zip function
# alwways return to list so we need to convert it into list.


roll = [100 ,55 ,66 ,88 ,105]
names = ["KS MAHIR" , "Mridul" , "MRINMOY" , "NAFISA" , "YANNA"]

a = list(zip(roll,names))
print (a)

#===============OUTPUT=================
#[(100, 'KS MAHIR'), (55, 'Mridul'), (66, 'MRINMOY'), (88, 'NAFISA'), (105, 'YANNA')]




#If one tuple contains more items, these items are ignored:
#use the tuple() function to display a readable version of the result:
a = ("John", "Charles", "Mike" , "MAHIR" , "LOL")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = tuple(zip(a, b))

print (x)
#===============OUTPUT=================
#(('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'), ('MAHIR', 'Vicky'))







# we can only add one letter of the string items to the list
roll = [100 ,55 ,66 ,88 ,105]
names = ["KS MAHIR" , "Mridul" , "MRINMOY" , "NAFISA" , "YANNA"]
a = list(zip(roll,names,"KSMAHIR"))
print (a)

#=====================OUTPUT============
#[(100, 'KS MAHIR', 'K'), (55, 'Mridul', 'S'), (66, 'MRINMOY', 'M'), (88, 'NAFISA', 'A'), (105, 'YANNA', 'H')]
