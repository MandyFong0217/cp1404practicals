"""
CP1404
unreliable_car class
Estimate time: 20min
Actual time: 20min
"""
from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """Specialised version of a Car that..."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = float(reliability)

    def drive(self, distance):
        if randint(0, 100) < self.reliability:
            super().drive(distance)
        return distance