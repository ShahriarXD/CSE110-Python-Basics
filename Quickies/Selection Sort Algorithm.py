a = [5,3,8,6,7,2]

for x in range(len(a)):
    minvalue = x
    for y in range(x, len(a)):
        if a[y] < a[minvalue]:
            minvalue = y
    if minvalue != x:
        a[minvalue] , a[x] = a[x] , a[minvalue]
    print(a)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
def sorted(a):
    for x in range(len(a)):
        minvalue = x
        for y in range(x, len(a)):
            if a[y] > a[minvalue]:
                minvalue = y
        if minvalue != x:
            a[minvalue] , a[x] = a[x] , a[minvalue]
            print(a)
    return a
a = [5,3,8,6,7,2]
print(sorted(a)) 








====================================
#todo Selection sort starts arranging the elements from the bottom
my_list=[10,1,20,3,6,2,5,11,15,2,12,14,17,18,29]
for i in range(len(my_list)-1):
  for j in range(0,len(my_list)-1-i):
    if my_list[j] > my_list[j+1]:
       temp = my_list[j]
       my_list[j] = my_list[j+1]
       my_list[j+1] = temp
  print(my_list)
print(my_list)



#todo - Bubble sort starts arranging the elements from the top
my_list = [10,1,20,3,6,2,5,11,15,2,12,14,17,18,29]
for i in range(len(my_list)-1):
  min_index  = i
  for j in range(i+1,len(my_list)):
    if my_list[j] < my_list[min_index]:
      min_index = j
  temp = my_list[i]
  my_list[i] = my_list[min_index]
  my_list[min_index] = temp
  print(my_list)
print(my_list)
