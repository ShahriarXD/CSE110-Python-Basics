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
