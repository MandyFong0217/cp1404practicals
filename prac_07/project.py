"""
CP1404 Intermediate Exercises
"""

import datetime


class Project:
    """Represent information about a programming language."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __repr__(self):
        return f" {self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, " \
               f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        return self.priority < other.priority
