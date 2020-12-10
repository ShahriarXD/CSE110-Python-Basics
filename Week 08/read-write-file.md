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
<p align="center">
  <img src="https://media.discordapp.net/attachments/764436939398185000/786573600307806229/Screenshot_2020-12-10_184215.png" title="hover text">
</p>

<p align="center">
  <img src="https://media.discordapp.net/attachments/764436939398185000/786574678675816468/unknown.png" title="hover text">
</p>

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




## It is a good practice to always close the file when you are done with it.
## Close the file when you are finish with it:

```bash
f = open("demofile.txt", "r")
print(f.readline())
f.close()
```
