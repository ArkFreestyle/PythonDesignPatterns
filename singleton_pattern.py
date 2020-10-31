"""
Singleton Pattern.
When you only want ONE instance of a class to exist throughout your code.

To test this code:
>>> o1 = OneOnly()
>>> o2 = OneOnly()
>>> o1 == o2
True
>>> o1
<__main__.OneOnly object at 0xb71c008c>
>>> o2
<__main__.OneOnly object at 0xb71c008c>

"""


class OneOnly:
    _singleton = None


    def __new__(cls, *args, **kwargs):
        """
        The __new__ method normally constructs a new instance of a class.
        but we'll be overriding it to return the same instance.
        """
        # If a single instance does not already exist
        if not cls._singleton:
            # Create one
            cls._singleton = super(OneOnly, cls).__new__(cls, *args, **kwargs)

        return cls._singleton