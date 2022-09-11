num_of_words = 0
num_of_Letters = 0
num_of_digits = 0

text = "My Name is Shakil 124"
for x in text:
    yy= x.upper()
    if yy >= "A" and yy <="Z":
        num_of_Letters+=1
    elif yy.isdigit():
        num_of_digits+=1
    elif yy == " ":
        num_of_words+=1

nono = text.split(" ")
print(len(nono))
print(num_of_words+1)
print(num_of_Letters)
print(num_of_digits)
