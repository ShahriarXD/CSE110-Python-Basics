import ast
a = ast.literal_eval(input())
bb = a.copy()
b = int(input())
c = len(a)
d = c/b
if b > d:
    print("Step size is not suitable")
else:
    a[0] = a[-1]
    a[2] = a[-3]
    xx = a.copy()
    xx[-1] = bb[0]
    xx[-3] = bb[2]
    print(xx)
