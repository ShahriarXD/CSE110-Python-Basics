def make_square(numbers):
    dict = {}
    for i in range(numbers[0],numbers[1]+1):
        temp = i*i
        dict[i] = temp
    print(dict)
make_square((1,3))
make_square((5,9))






# def make_square(a,b):
#     dict = {}
#     for i in range(a,b+1):
#         temp = i*i
#         dict[i] = temp
#     print(dict)
# make_square(1,3)
# make_square(5,9)
