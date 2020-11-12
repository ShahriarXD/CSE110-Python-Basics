# to revers any thing we use [::-1]

# Example: 

n = input()[::-1]
print(n)


b = "ALIF"[::-1]
print (b)





txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for x in words:
    t.append((len(x), x))
t.sort(reverse=True)
print(t)
#=============================
[(6, 'yonder'), (6, 'window'), (6, 'breaks'), (5, 'light'), (4, 'what'), (4, 'soft'), (3, 'but'), (2, 'in')]
