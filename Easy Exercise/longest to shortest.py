txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for x in words:
    t.append((len(x), x))
t.sort(reverse=True)
print(t)
final = list()
for y,z in t:
    final.append(z)
print(final)
