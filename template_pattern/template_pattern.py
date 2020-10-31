"""
The template pattern is useful for removing duplicate code; it's an implementation
to support the Don't Repeat Yourself principle.

It is designed for situations where we have several different tasks to accomplish that
have some, but not all, steps in common.

The common steps are implemented in a base class, and the distinct steps are overridden
in subclasses to provide custom behavior.

We're going to create a car sales reporter as an example.
"""

import sqlite3
import datetime

# Database setup, create a table and insert values.

conn = sqlite3.connect("sales.db")
try:
    conn.execute("CREATE TABLE Sales(salesperson text, amt currency, year integer, model text, new boolean)")
except sqlite3.OperationalError:
    pass
conn.execute("INSERT INTO Sales values('Tim', 16000, 2010, 'Honda Fit', 'true')")
conn.execute("INSERT INTO Sales values('Tim', 9000, 2006, 'Ford Focus', 'false')")
conn.execute("INSERT INTO Sales values('Gayle', 8000, 2004, 'Dodge Neon', 'false')")
conn.execute("INSERT INTO Sales values('Gayle', 28000, 2009, 'Ford Mustang', 'true')")
conn.execute("INSERT INTO Sales values('Gayle', 50000, 2010, 'Lincoln Navigator', 'true')")
conn.execute("INSERT INTO Sales values('Don', 20000, 2008, 'Toyota Prius', 'false')")
conn.commit()
conn.close()


class QueryTemplate:
    def connect(self):
        self.conn = sqlite3.connect("sales.db")

    def construct_query(self):
        raise NotImplementedError()

    def do_query(self):
        results = self.conn.execute(self.query)
        self.results = results.fetchall()

    def format_results(self):
        output = []
        for row in self.results:
            row = [str(i) for i in row]
            output.append(", ".join(row))

        self.formatted_results = "\n".join(output)

    def output_results(self):
        raise NotImplementedError()

    def process_format(self):
        self.connect()
        self.construct_query()
        self.do_query()
        self.format_results()
        self.output_results()


class NewVehiclesQuery(QueryTemplate):
    def construct_query(self):
        self.query = "select * from Sales where new='true'"

    def output_results(self):
        print(self.formatted_results)


class UserGrossQuery(QueryTemplate):
    def construct_query(self):
        self.query = ("select salesperson, sum(amt) from Sales group by salesperson")

    def output_results(self):
        filename = f"gross_sales_{datetime.date.today().strftime('%Y%m%d')}.txt"
        with open(filename, 'w') as outfile:
            outfile.write(self.formatted_results)


if __name__ == "__main__":
    # Prints the new vehicles
    new_vehicles = NewVehiclesQuery()
    new_vehicles.process_format()
    new_vehicles.output_results()

    # Writes gross amount for each person to a file
    gross_amt = UserGrossQuery()
    gross_amt.process_format()
    gross_amt.output_results()