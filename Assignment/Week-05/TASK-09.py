exam_marks = {'Cierra Vega': 175, 'Alden Cantrell': 200, 'Kierra Gentry': 165, 'Pierre Cox': 190}
a = int(input())
dict = {}
for x, y in exam_marks.items():
    if y >= a:
        dict[x] = y 
print(dict)


# exam_marks = {'Cierra Vega': 175, 'Alden Cantrell': 200, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# a = int(input())
# Final = {x : y for x,y in exam_marks.items() if y == a or y>a}
# print(Final)
