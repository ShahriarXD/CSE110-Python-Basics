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






sex= [1,5,6,5,2,5,26,6]
a = [x for x in sex]
print (a)

sex1= [1,5,6,5,2,5,26,6]
b = [x+5 for x in sex1]
print(b)

sex2= [1,5,6,5,2,5,26,6]
c = [x for x in sex2 if x>5]
print(c)
