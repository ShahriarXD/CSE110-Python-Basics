#we cannot change the value of a tupe.
#but what we can do is we can replace the value of it


t = ('a', 'b', 'c', 'd', 'e')
t = ('A',) + t[1:]
print(t)

#========Output==========
('A', 'b', 'c', 'd', 'e')
