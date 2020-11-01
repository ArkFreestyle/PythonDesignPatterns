"""
The abstract factory pattern is normally used when we have
multiple possible implementations of a system that depend on
some configuration or platform issue.

The calling code requests an object from the abstract factory,
not knowing exactly what class of object will be returned.

Common examples of the abstract factory pattern include code for
operating-system independent toolkits, database backends,
and country-specific formatters or calculators.

Django provides an abstract factory that returns a set of
object relational classes for interacting with a specific
database backend (MySQL, PostgreSQL, SQLite, and others)
depending on a configuration setting for the current site.
If the application needs to be deployed in multiple places,
each one can use a different database backend by changing
only one configuration variable.

Again, you'll notice there's a lot of repeated boilerplate,
so this isn't the most pythonic way to do things.
"""

# Create the formatters


class FranceDateFormatter:
    def format_date(self, y, m, d):
        y, m, d = (str(x) for x in (y,m,d))
        y = '20' + y if len(y) == 2 else y
        m = '0' + m if len(m) == 1 else m
        d = '0' + d if len(d) == 1 else d
        return(f"{d}/{m}/{y}")


class USADateFormatter:
    def format_date(self, y, m, d):
        y, m, d = (str(x) for x in (y, m, d))
        y = '20' + y if len(y) == 2 else y
        m = '0' + m if len(m) == 1 else m
        d = '0' + d if len(d) == 1 else d
        return (f"{m}-{d}-{y}")


class FranceCurrencyFormatter:
    def format_currency(self, base, cents):
        base, cents = (str(x) for x in (base, cents))

        if len(cents) == 0:
            cents = '00'

        elif len(cents) == 1:
            cents = '0' + cents

        digits = []

        for i, c in enumerate(reversed(base)):
            if i and not i % 3:
                digits.append(' ')
            digits.append(c)

        base = ''.join(reversed(digits))

        return f'{base}€{cents}'


class USACurrencyFormatter:
    def format_currency(self, base, cents):
        base, cents = (str(x) for x in (base, cents))

        if len(cents) == 0:
            cents = '00'

        elif len(cents) == 1:
            cents = '0' + cents

        digits = []

        for i, c in enumerate(reversed(base)):
            if i and not i % 3:
                digits.append(',')
            digits.append(c)

        base = ''.join(reversed(digits))

        return f'${base}.{cents}'


# Now create the factories


class USAFormatterFactory:
    def create_date_formatter(self):
        return USADateFormatter()

    def create_currency_formatter(self):
        return USACurrencyFormatter()


class FranceFormatterFactory:
    def create_date_formatter(self):
        return FranceDateFormatter()

    def create_currency_formatter(self):
        return FranceCurrencyFormatter()


country_code = "US"

factory_map = {
    "US": USAFormatterFactory,
    "FR": FranceFormatterFactory
}

formatter_factory = factory_map.get(country_code)()