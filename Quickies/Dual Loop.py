a = [5,3,8,6,7,2]

for x in range(len(a)):
    minvalue = x
    for y in range(x+1, len(a)):
        print(y)


1
2
3
4
5
2
3
4
5
3
4
5
4
5
5


a = [5,3,8,6,7,2]

for x in range(len(a)):
    minvalue = x
    for y in range(x, len(a)):
        print(y)



0
1
2
3
4
5
1
2
3
4
5
2
3
4
5
3
4
5
4
5
5






a = [5,3,8,6,7,2]
for x in range(len(a)):
    for y in range(len(a)):
        print(y)
        
        
0
1
2
3
4
5
0
1
2
3
4
5
0
1
2
3
4
5
0
1
2
3
4
5
0
1
2
3
4
5
0
1
2
3
4
5
