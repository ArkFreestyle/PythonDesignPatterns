"""
The iterator pattern provides a way to access elements of an object without needing to know its underlying representation.
Think of common data structures like lists, tuples and sets that python lets you iterate over.
If you wanted to create your own data structure (without inheriting from these default ones) while being able to iterate over it,
this is how you would do it!

Python makes full use of this pattern in iteration related areas, such as comprehensions (list, dict, set, generator).

Usage of the classes in here:

Iterable and Iterator (use this if you want to keep both separate):

>>> x = Iterable("yo momma so fat")
>>> for thing in x:
...     print(thing)

YO
MOMMA
SO
FAT

IterableAndIterator (use this for a 2-in-1 solution lol):

>>> x = IterableAndIterator("HI LMAO WHAT THE HECK IS THIS")
>>> for thing in x:
...     print(thing)

HI
LMAO
WHAT
THE
HECK
IS
THIS
"""

class Iterable:
    """This is what you want to iterate over"""

    def __init__(self, string):
        self.string = string
    
    def __iter__(self):
        """Here's where you define how to iterate over your iterable"""
        
        return Iterator(self.string)


class Iterator:
    """This is what lets you loop over your iterable"""

    def __init__(self, string):
        self.words = [x.upper() for x in string.split()]
        self.index = 0
    
    def __next__(self):
        if self.index == len(self.words):
            raise StopIteration()
        
        word = self.words[self.index]
        self.index += 1
        return word


class IterableAndIterator:
    """Trying to make a class that does both lol"""

    def __init__(self, string):
        self.string = string
        self.words = [x.upper() for x in string.split()]
        self.index = 0

    def __next__(self):
        if self.index == len(self.words):
            raise StopIteration()
        
        word = self.words[self.index]
        self.index += 1
        return word

    def __iter__(self):
        """I AM THE ITERATOR LMAO"""
        return self
