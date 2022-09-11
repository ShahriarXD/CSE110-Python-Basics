# TO IMP DATA STUCTURE WICH IS STACK AND QUEUE
# In stack we can store data and access it (push and pop)
# stack onk ta boi we opor boi rakhar moto kaj kore
# mane ektar opor r ekta
# r pop korle uprer theke ber hobe
# So ei process ta is like LIFO ( Last In First Out)


books = []
books.append("C")
books.append("C++")
books.append("JAVA")
print(books)
books.pop()
print(books)


# =======================================================

# QUEUE = (Ulta first in first out)
# eitate hobe .popleft()

from collections import deque


bank = deque( ["a","x","y"])

bank.popleft()
print(bank)
