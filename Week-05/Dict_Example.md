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




