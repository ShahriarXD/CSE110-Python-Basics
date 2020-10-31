## Basic List Operation : 

<p align="center">
  <img src="https://media.discordapp.net/attachments/770868718132658206/772067341831241728/unknown.png" title="hover text">
</p>

```python
#Extending
losit = ["Rafin" , "Messi", "Bill Gates" , "MAHIR" , "YANNA"]
sex = [1 , 5 , 5,6,4,56,4]
a = losit.extend(sex)
print(losit)     #here we can extend a certain list but cant make a value of new list
#ADDING
losit = ["Rafin" , "Messi", "Bill Gates" , "MAHIR" , "YANNA"]
sex = [1 , 5 , 5,6,4,56,4]
a = losit + sex
print(a)
#Repitation
losit = ["Rafin" , "Messi", "Bill Gates" , "MAHIR" , "YANNA"]
print(losit*2)
#Slicing list[start:end:step]
losit = ["Rafin" , "Messi", "Bill Gates" , "MAHIR" , "YANNA"]
a = losit[1:-1]
print (a)
losit = ["Rafin" , "Messi", "Bill Gates" , "MAHIR" , "YANNA"]
a = losit[:-1]
print (a)
losit = ["Rafin" , "Messi", "Bill Gates" , "MAHIR" , "YANNA"]
a = losit[:]
print (a)
losit = ["Rafin" , "Messi", "Bill Gates" , "MAHIR" , "YANNA"]
a = losit[:-1:2]
print (a)
#loop
losit = ["Rafin" , "Messi", "Bill Gates" , "MAHIR" , "YANNA"]
for x in losit:
    print(x , end=",")
print ("")
#Items in
losit = ["Rafin" , "Messi", "Bill Gates" , "MAHIR" , "YANNA"]
a = "Rafin" in losit
print (a)
```

```bash
['Rafin', 'Messi', 'Bill Gates', 'MAHIR', 'YANNA', 1, 5, 5, 6, 4, 56, 4]
['Rafin', 'Messi', 'Bill Gates', 'MAHIR', 'YANNA', 1, 5, 5, 6, 4, 56, 4]
['Rafin', 'Messi', 'Bill Gates', 'MAHIR', 'YANNA', 'Rafin', 'Messi', 'Bill Gates', 'MAHIR', 'YANNA']
['Messi', 'Bill Gates', 'MAHIR']
['Rafin', 'Messi', 'Bill Gates', 'MAHIR']
['Rafin', 'Messi', 'Bill Gates', 'MAHIR', 'YANNA']
['Rafin', 'Bill Gates']
Rafin,Messi,Bill Gates,MAHIR,YANNA,
Tru
```

```
<p align="center">
  <img src="https://media.discordapp.net/attachments/770868718132658206/772071715378561054/unknown.png" title="hover text">
</p>
