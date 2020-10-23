#Comprehension Fuction
#[expression for item in list]


SEX = [ 55 ,66 ,88 , 5555]
RESULT = [x for x in SEX]
print(RESULT)


SEX1 = [ 55 ,65 ,85 , 5555]
RESULT1 = [x+5 for x in SEX1]
print(RESULT1)

SEX1 = [ 55 ,65 ,85 , 5555]
RESULT1 = [x for x in SEX1 if x>60]
print(RESULT1)

SEX1 = [ 55 ,65 ,85 , 5555]
RESULT1 = [x+5 for x in SEX1 if x%2 == 0]
print(RESULT1)




# =============================OUTPUT=================
# [55, 66, 88, 5555]
# [60, 70, 90, 5560]
# [65, 85, 5555]    
# []
