s1 = input("")
s2 = input("")
newString = ""
lenS1 = len(s1)
lenS2 = len(s2)
if len(s1) == len(s2):
    for i in range(lenS1):
        newString += s1[i] + s2[i]
    print (newString)
else:
    lenToDo = min(lenS1, lenS2)
    for i in range(lenToDo):
        newString += s1[i] + s2[i]
    if lenS1 > lenS2:
        newString += s1[lenS2:]
    else:
        newString += s2[lenS1:]
    print (newString)
    
#ALSO SEE
#https://github.com/ShahriarXD/CSE110-Python-Basics/blob/main/Later_Solve/w3%20T5.py
