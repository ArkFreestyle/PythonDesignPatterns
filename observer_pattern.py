"""
The observer pattern is useful for state monitoring.

It allows a given object to be monitored by a dynamic group of 'observer' objects.
Each observer doesn't care about other observers.

When something changes on the observed object, the update() method is called on all observers,
so all of them know that a change has occurred.

Each observer could be responsible for different tasks when the core object changes.

Usage:
>>> i = Inventory()
>>> c1 = ConsoleObserver(i)
>>> c2 = ConsoleObserver(i)
>>> i.attach(c1)
>>> i.attach(c2)
>>> i.product = "Gadget"
Gadget
0
Gadget
0

The observer pattern detaches the code being observed from the code doing the observing.

Achieving this same functionality without this pattern would mean lots of conditions when setting
any property, both maintenance and addition of features would become really painful eventually.
"""


class Inventory:
    def __init__(self):
        self.observers = []
        self._product = None
        self._quantity = 0
    
    def attach(self, observer):
        self.observers.append(observer)

    @property
    def product(self):
        return self._product
    
    @product.setter
    def product(self, value):
        self._product = value
        self._update_observers()
    
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        self._quantity = value
        self._update_observers()

    def _update_observers(self):
        for observer in self.observers:
            observer()


class ConsoleObserver:
    def __init__(self, inventory):
        self.inventory = inventory
    
    def __call__(self):
        print(self.inventory.product)
        print(self.inventory.quantity)
