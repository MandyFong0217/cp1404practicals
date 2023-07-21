"""
CP1404 Intermediate Exercises
"""


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Car instance.

        fuel: float, one unit of fuel drives one kilometre
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return str(f"My guitar: {self.name}, first made in {self.year}")

    def get_age(self):
        this_year = 2022
        return this_year - self.year

    def is_vintage(self):
        if Guitar.get_age(self) >= 50:
            return True
        else:
            return False
