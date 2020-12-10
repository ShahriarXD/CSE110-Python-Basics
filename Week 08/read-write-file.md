## File in TXT : 

```bash
By default the read() 
method returns 
the whole text,
but you can also 
specify how
many characters 
you want to return:
```

```python
f = open("demofile.txt", "r")
print(f.read())

f = open("D:\\myfiles\demofile.txt", "r")
print(f.read())

```

```bash
OUTPUT :  


By default the read() 
method returns        
the whole text,       
but you can also      
specify how
many characters       
you want to return:
```

```python
f = open("demofile.txt", "r")
print(f.read(15))
```

```bash
By default the 
```

```python
f = open("demofile.txt", "r")
print(f.readline())



f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())
```
```bash
By default the read() 

By default the read() 

method returns   
```

```python
f = open("demofile.txt", "r")
for x in f:
  print(x)
```  

```bash
By default the read() 

method returns 

the whole text,

but you can also

specify how

many characters

you want to return:
``` 
