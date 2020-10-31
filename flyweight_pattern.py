"""
The flyweight pattern is a memory optimization pattern.

The flyweight pattern basically ensures that objects that share a state can use the
same memory for that shared state. It is often implemented only after a program
has demonstrated memory problems.

We're implementing an inventory system for cars now.

Create two car models.
>>> dx = CarModel("FIT DX")
>>> lx = CarModel("FIT LX", air=True, cruise_control=True, power_locks=True, tilt=True)
>>> car1 = Car(dx, "blue", "12345")
>>> car2 = Car(dx, "black", "12346")
>>> car3 = Car(lx, "red", "12347")

Delete one of them (this step has no significance)
>>> id(lx)
>>> del lx
>>> del car3
>>> import gc
>>> gc.collect()

Create two car models with the same name. (it'll be the same object!)
Check their ids, it's the same object! BOOM, memory conserved.
>>> lx = CarModel("FIT LX", air=True, cruise_control=True, power_locks=True, tilt=True)
>>> id(lx)
>>> lx = CarModel("FIT LX")
>>> id(lx)
>>> lx.air
"""

import weakref


class CarModel:
    # Entries in a weak value dictionary are discarded when unreferenced.
    _models = weakref.WeakValueDictionary()

    def __new__(cls, model_name, *args, **kwargs):
        model = cls._models.get(model_name)
        if not model:
            model = super().__new__(cls)
            cls._models[model_name] = model

        return model

    def __init__(self,
                 model_name,
                 air=False,
                 tilt=False,
                 cruise_control=False,
                 power_locks=False,
                 alloy_wheels=False,
                 usb_charger=False):

        if not hasattr(self, "initted"):
            self.model_name = model_name
            self.air = air
            self.tilt = tilt
            self.cruise_control = cruise_control
            self.power_locks = power_locks
            self.alloy_wheels = alloy_wheels
            self.usb_charger = usb_charger
            self.initted = True

    def check_serial(self, serial_number):
        print(f"Sorry, we are unable to check the serial number {serial_number} on the {self.model_name} at this time")


class Car:
    def __init__(self, model, color, serial):
        self.model = model
        self.color = color
        self.serial = serial

    def check_serial(self):
        return self.model.check_serial(self.serial)
