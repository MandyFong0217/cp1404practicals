"""
CP1404 Intermediate Exercises
"""


class ProgrammingLanguage:
    """Represent a Car object."""

    def __init__(self, name='', typing='', reflection='', year=''):
        """Initialise a Car instance.

        fuel: float, one unit of fuel drives one kilometre
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == 'Dynamic':
            return True

    def __str__(self):
        return str(f'{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}')
