"""
The decorator pattern allows behavior to be added to an individual object, dynamically, 
without affecting the behavior of other objects from the same class.

Q) How does the wrapper get args and kwargs???

Because the decorator is essentially doing this: 

make_call = log_calls(make_call)

so even though it looks like you're calling make_call you're actually calling wrapper
since log_calls returns wrapper. So the new make_call is wrapper and so wrapper
receives the args and kwargs you pass to make_call. – mVChr (comment from stackoverflow)

Q) Why use a nested function inside the decorator? Why not just do this:
def log_calls(func):
    print("do something before function")
    func()
    print("do something after function")

and call log_calls()?

Because you just created another function which does something before calling another function. It's not a DECORATOR.
A decorator RETURNS a function, that's what allows you to use the @decorator syntax too, you can't use that with this example.

With a decorator you are CALLING the decorator's inner (wrapper) function. Here's how it plays out:

some_function = decorator(some_function) becomes,
some_function = wrapper

When you call some_function with its arguments:
some_function(1, 2, 3) it means,
wrapper(1, 2, 3) which returns what?
some_function(1, 2, 3) but it does stuff before and after it!
DECORATORS, LADIES AND GENTLEMEN.

"""

def log_calls(func):
    """This will act as a decorator"""
    
    def wrapper(*args, **kwargs):
        """The args and kwargs here will be the decorated function's arguments"""

        print(f"Decorator calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        function_to_return = func(*args, **kwargs)
        print("Logged the call! (Done by the decorator)")
        return function_to_return
        
    return wrapper


# Decorate make_call using python's decorator syntax


@log_calls
def make_call(a, b, c, number=123):
    print("Making a call...")
    print("Call ended.")


make_call(1, 2, c=3)


# Decorate make_call manually:


# def make_call(a, b, c, number=123):
#     print("Making a call...")
#     print("Call ended.")


# make_call = log_calls(make_call)
# make_call(1, 2, c=3)


# Doesn't work: raises a TypeError: 'NoneType' object is not callable
# def wrong_decorator(func):
#     print("Before the func")
#     func()
#     print("After the func")


# @wrong_decorator
# def test():
#     print("func-y!!!")

# The next line raises an error:
# test()