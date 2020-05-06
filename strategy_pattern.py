"""
The strategy pattern enables a client class to choose between different algorithms.
To make an object oriented program choose between different algorithms often requires way too
many if else conditions. This is a much neater way of getting the same thing done.

So what you do is basically create different classes of the algorithms you want to choose from, strategy classes.
(You could make them functions too, since functions are objects in python and can be assigned to variables)

This pattern decouples the client class from the strategy classes.

Usage:

>>> elephant = Animal(name="Elephant", walk=FourLegWalk)
>>> cobra = Animal(name="Cobra", walk=SnakeWalk)
>>> human = Animal(name="Homo Sapien", walk=TwoLegWalk)

>>> elephant.walk()
I am using all four of my legs to walk because I am a 4 legged animal.
>>> cobra.walk()
I am slithering side to side because I am a snake.
>>> human.walk()
I am standing up on my two legs to walk because I am a 2 legged animal.

"""


class Animal:
    
    def __init__(self, name=None, walk=None):
        self.name = name
        self.walk_strategy = walk

    def walk(self):
        """
        Cause animal instance to walk
        
        Walking funcionality is a strategy, and is intended to
        be implemented separately by different types of animals.
        """
        
        if self.walk_strategy is None:
            message = '{} should implement a walk method'.format(self.__class__.__name__)
            raise NotImplementedError(message)
        
        else:
            self.walk_strategy().walk()


# Here are some different walking algorithms that can be used with Animal


class SnakeWalk:
    def walk(self):
        print('I am slithering side to side because I am a snake.')


class FourLegWalk:
    def walk(self):
        print('I am using all four of my legs to walk because I am a 4 legged animal.')


class TwoLegWalk:
    def walk(self):
        print('I am standing up on my two legs to walk because I am a 2 legged animal.')
