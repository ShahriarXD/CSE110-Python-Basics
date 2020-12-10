## Write to an Existing File
 
```bash
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content
```

```python
f = open("demofile.txt", "r")
for x in f:
    print(x ,end="")
f.close()
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

## Start

```python
f = open("shahriar.txt", "w")
f.write("Now the file has more content!\n")
f.write("copyright\n")
f.write("By Shahriar")
f = open("shahriar.txt", "r")
print(f.read())
f.close()
```

```bash
Now the file has more content!
copyright
By Shahriar
```
