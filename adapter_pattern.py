"""
The adapter pattern is designed to interact with existing code.

Adapters are used to allow two pre-existing objects to work together,
even if their interfaces are not compatible.

Like the display adapters that allow VGA projectors to be plugged into
HDMI ports, an adapter object sits between two different interfaces, translating
between them on the fly.

The adapter object's sole purpose is to perform this translation job.

Let's build an age calculator that takes a string date,
and then build an adapter for it that will accept datetime objects.
>>> a = DateAgeAdapter(datetime.date(1975, 1, 12))
>>> a.get_age(datetime.date.today())
"""

import datetime


class AgeCalculator:
    def __init__(self, birthday):
        self.year, self.month, self.day = (int(x) for x in birthday.split('-'))

    def calculate_age(self, date):
        year, month, day = (int(x) for x in date.split('-'))
        age = year - self.year

        if (month, day) < (self.month, self.day):
            age -= 1

        return age


class DateAgeAdapter:
    def _str_date(self, date):
        return date.strftime("%Y-%m-%d")

    def __init__(self, birthday):
        birthday = self._str_date(birthday)
        self.calculator = AgeCalculator(birthday)

    def get_age(self, date):
        date = self._str_date(date)
        return self.calculator.calculate_age(date)
