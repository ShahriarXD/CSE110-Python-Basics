## Iterator, Iterable, and Iteration

## Iteration: 

```bash
is a general term for taking each item of something, one after another. 
Any time you use a loop, explicit or implicit, to go over a group of items, that is iteration.
```
## Iterable:
```bash
An iterable is an object that has an __iter__ method which returns an iterator, 
or which defines a __getitem__ method that can take sequential indexes starting from zero 
(and raises an IndexError when the indexes are no longer valid). 
So an iterable is an object that you can get an iterator from.
```

## Iterator:
```bash
An iterator is an object with a next (Python 2) or __next__ (Python 3) method.
Whenever you use a for loop, or map, or a list comprehension, etc. in Python, 
the next method is called automatically to get each item from the iterator, thus going through the process of iteration
```
