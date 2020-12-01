def selection(a):
    for x in range(len(a)):
        #find minimup and swap with a[x]
        min_index = x
        min = a[x]
        for y in range(x+1, len(a)):
            if a[y]<min:                 #for desending one logic if a[y]>min: > then hobe
                min = a[y]
                min_index = y
        temp = a[min_index]
        a[min_index] = a[x]
        a[x] = temp
    return a
print(selection([3,5,5,656,-5,4,5,5,5,55]))
