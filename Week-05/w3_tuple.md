<p align="center">
  <img src="https://media.discordapp.net/attachments/770868718132658206/777936046604288050/unknown.png" title="hover text">
</p>

```python
thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(thistuple[0])

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
```

```bash
('apple', 'banana', 'cherry')
apple
cherry
('cherry', 'orange', 'kiwi')
```

## Change Tuple Values :

```python
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
```

```bash
('apple', 'kiwi', 'cherry')
```

## Join Two Tuples : 

```python
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
```

```bash
('a', 'b', 'c', 1, 2, 3)
```

```python
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(len(thistuple))

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)
```

```bash
2
10
3 
```
