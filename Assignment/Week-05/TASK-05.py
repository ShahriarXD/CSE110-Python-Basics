tuple = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2) 
count = 0
usr_inp = int(input())
for x in tuple:
    if (x == usr_inp):
        count = count + 1
print(f"{usr_inp} appears {count} times in the tuple")
