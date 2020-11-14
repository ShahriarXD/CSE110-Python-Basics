import ast
a = ast.literal_eval(input())
sum = 0
count = 0
for x,y in a.items():
    sum += y
    count += 1
avg = sum/count
Final  = round(avg)
print(f"Average is {Final}")

#a = {'Jon': 100, 'Dan':200, 'Rob':30}
# sum = 0
# for x in a.values():
#     sum = sum + x
# avg = 0
# for x in a:
#     avg += 1
# Final = sum/avg
# zz =round(Final)
# print(f"Average is {zz}")
