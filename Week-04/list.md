## LIST ACESSING :

<p align="center">
  <img src="https://media.discordapp.net/attachments/770868718132658206/772064233365307392/unknown.png" title="hover text">
</p>

<p align="center">
  <img src="https://media.discordapp.net/attachments/770868718132658206/772064954303774740/unknown.png?width=1442&height=362" title="hover text">
</p>

```python
losit = ["Rafin" , "Messi", "Bill Gates" , "MAHIR" , "YANNA"]
losit[3] = "NAFISA"
losit[1] = "Princila"
print (losit)
```

```bash
['Rafin', 'Princila', 'Bill Gates', 'NAFISA', 'YANNA']
```

## Python Collections (Arrays):
```bash
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
```
## Access Items:
```python
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
```
```bash
banana
cherry
```

## Range of Indexes:
```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#This will return the items from position 2 to 5.
#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included



thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
#This will return the items from index 0 to index 4.
#Remember that index 0 is the first item, and index 4 is the fifth item
#Remember that the item in index 4 is NOT included



thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
#This will return the items from index 2 to the end.
#Remember that index 0 is the first item, and index 2 is the third



thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#Negative indexing means starting from the end of the list.
#This example returns the items from index -4 (included) to index -1 (excluded)
#Remember that the last item has the index -1,
```
```bash
['cherry', 'orange', 'kiwi']
['apple', 'banana', 'cherry', 'orange']
['cherry', 'orange', 'kiwi', 'melon', 'mango']
['orange', 'kiwi', 'melon']
```

## Change Item Value:
```python
# To change the value of a specific item, refer to the index number:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
```
```bash
['apple', 'blackcurrant', 'cherry']
```
## Check if Item Exists:
```python
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
```
```bash
Yes, 'apple' is in the fruits list
```
## List Length:
```python
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
```
```bash
3
```



<p align="center">
  <img src="https://media.discordapp.net/attachments/770868718132658206/771015746049933312/unknown.png" title="hover text">
</p>

## append() Method = appends an element to the end of the list.
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)
```
```bash
['apple', 'banana', 'cherry', 'orange']
```
## List copy() Method = returns a copy of the specified list.
```python
fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x)
```
```bash
['apple', 'banana', 'cherry']
```
## List clear() Method = removes all the elements from a list.
```python
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)
```
```bash
[]
```
## List count() Method = returns the number of elements with the specified value.
```python
fruits = ["apple", "banana", "cherry"]
x = fruits.count("cherry")
print(x)

points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x)
```
```bash
1
2
```
## List extend() Method = adds the specified list elements (or any iterable) to the end of the current list.
```python
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)
```
```bash
['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']
```
## List index() Method = returns the position at the first occurrence of the specified value.
```python
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)
```
```bash
2
```
## List insert() Method = inserts the specified value at the specified position.
```python
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)
```
```bash
['apple', 'orange', 'banana', 'cherry']
```
## List pop() Method = removes the element at the specified position.
```python
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)
```
```bash
['apple', 'cherry']
```
## List remove() Method = removes the first occurrence of the element with the specified value.
```python
fruits = ['apple', 'banana', 'cherry' ,'banana']
fruits.remove("banana")
print(fruits)
```
```bash
['apple', 'cherry', 'banana']
```
## List reverse() Method = reverses the sorting order of the elements.
```python
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)
```
```bash
['cherry', 'banana', 'apple']
```
## List sort() Method =  sorts the list ascending by default.
```python
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)
```
```bash
['BMW', 'Ford', 'Volvo']
```

# For more Visit:
[List Methods](https://www.w3schools.com/python/python_ref_list.asp)

[List sort()](https://www.w3schools.com/python/ref_list_sort.asp)
