import ast
a = ast.literal_eval(input())
max = 0
for x,y in a.items():
    if y > max:
        max = y
        if y == max:
            genre =  x
print(f"The highest selling book genre is {genre} and the number of books sold are {max}")
