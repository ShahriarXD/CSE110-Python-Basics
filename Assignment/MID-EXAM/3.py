list = ['A','B', 'C', 'D', 'E', 'F','G','H']
step = int(input())
if len(list)/2 < step:
    print("Step size is not suitable")
else:
    for x in range(0,len(list)//2 , step):
        temp = list[x]
        list[x] = list[-x-1]
        list[-x-1] = temp
print(list)
