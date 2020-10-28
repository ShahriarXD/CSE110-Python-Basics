## 1. replace()	= Returns a string where a specified value is replaced with a specified value.
```python
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
```
```bash
I like apples
```
## 2. capitalize()	= Converts the first character to upper case.
```python
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)
```
```bash
Hello, and welcome to my world.
```
## 3. casefold()	= Converts string into lower case.
```python
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)
```
```bash
hello, and welcome to my world!
```
## 4. count()	= Returns the number of times a specified value occurs in a string.
```python
txt = "I love apples, applesss apples3333 are my favorite fruit"
x = txt.count("apples")
print(x)
```
```bash
3
```
## 5. startswith() method returns True if the string starts with the specified value.
```python
txt = "Hello, welcome to my world."
if txt.startswith("welcome"):
	print(55+55)
else:
	print("Sexy")
txt = "Hello, welcome to my world."
if txt.startswith("Hello"):
	print(55+55)
else:
	print("Sexy")
```
```bash
Sexy
110
```
## 6. endswith() = method returns True if the string ends with the specified value.
```python
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)
```
```bash
True
```
## 7. find() = method finds the first occurrence of the specified value.
```python
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)
```
```bash
#The find() method returns -1 if the value is not found.
#The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found.
7
```
## 8. index() = method finds the first occurrence of the specified value.
```python
txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)
```
```bash
7
```
## 9. join() = method takes all items in an iterable and joins them into one string.
```python
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

txt = "banana"
x = "#".join(txt)
print(x)
```
```bash
John#Peter#Vicky
b#a#n#a#n#a
```
## 9. partition() = method searches for a specified string, and splits the string into a tuple.
```bash
Search for the word "bananas", and return a tuple with three elements:

1 - everything before the "match"
2 - the "match"
3 - everything after the "match"
```
```python
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

txt = "I could eat bananas all day
x = txt.partition("apples")
print(x)
```
```bash
('I could eat ', 'bananas', ' all day')
('I could eat bananas all day', '', '')
```
## 10. upper()/lower() = method returns a string where all characters are in upper/lower case.
```python
txt = "Hello my friends"
x = txt.upper()
print(x)


txt = "Hello my friends"
x = txt.lower()
print(x)
```
```bash
HELLO MY FRIENDS
hello my friends
```
