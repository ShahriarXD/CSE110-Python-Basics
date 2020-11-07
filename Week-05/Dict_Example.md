## Important :

```python
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for key, value in car.items():
    print(key , value) 
```
```bash
brand Ford
model Mustang  
year 1964  
```


## Dictionary: A collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
```
```bash
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
```

## Accessing Items: access the items of a dictionary by referring to its key name, inside square brackets.
```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
```
```bash
Mustang
```
```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)
```
```bash
Mustang
```
## Change Values: changing the value of a specific item by referring to its key name.
```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2018

print(thisdict)
```
```bash
{'brand': 'Ford', 'model': 'Mustang', 'year': 2018}
```
## Loop Through a Dictionary:
```python
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
  
  
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])  
  
  
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)  
  
  
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)
  
  
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)  
```
```bash
brand
model
year

==============
Ford
Mustang
1964

=============
Ford
Mustang
1964

===========


brand Ford
model Mustang  
year 1964 
```

<p align="center">
  <img src="https://media.discordapp.net/attachments/770868718132658206/774619226606272522/unknown.png?width=400&height=677" title="hover text">
</p>

## Check if Key Exists:
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "brand" in thisdict:
    print(True)
```
```bash
True
```

## Dictionary Length :
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(thisdict))
```
```bash
3
```
## Adding Items : 
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
```
```bash
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
```
## Removing Items :
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "sex":69
}
thisdict.popitem()     #popitem() method removes the last inserted item
thisdict.pop("model")  
print(thisdict)
```
```bash
{'brand': 'Ford', 'year': 1964}
```
## Del/Clear/Copy :
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


#Make a copy of a dictionary with the dict() function:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
```
```bash
{}
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
```

## Learn More :
[Click Here <====](https://www.w3schools.com/python/python_dictionaries.asp)

