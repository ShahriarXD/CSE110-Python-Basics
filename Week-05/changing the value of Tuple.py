#we cannot change the value of a tupe.
#but what we can do is we can replace the value of it


t = ('a', 'b', 'c', 'd', 'e')
t = ('A',) + t[1:]
print(t)




t = ('a', 'b', 'c', 'd', 'e')
new_tuple_after_changing = ("BOSS",) + t[0:]
print(new_tuple_after_changing)

t = ('a', 'b', 'c', 'd', 'e')
new_tuple_after_changing = ("BOSS",) + t[1:]
print(new_tuple_after_changing)


t = ('a', 'b', 'c', 'd', 'e')
new_tuple_after_changing = ("BOSS",) + t[4:]
print(new_tuple_after_changing)

#========Output==========
('A', 'b', 'c', 'd', 'e')


('BOSS', 'a', 'b', 'c', 'd', 'e')
('BOSS', 'b', 'c', 'd', 'e')
('BOSS', 'e')
