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
