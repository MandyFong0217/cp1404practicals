"""
CP1404
silver service taxi class
Estimate time: 1hr
Actual time: 1hr
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.name = name
        self.fuel = fuel
        self.fanciness = float(fanciness) * self.price_per_km

    def __str__(self):
        self.price_per_km = self.fanciness
        return f'{super().__str__()} plus flagfall of ${self.flagfall:.2f}'

    def drive(self, distance):
        self.fuel = float(self.fuel)
        self.odometer = float(self.odometer)
        self.current_fare_distance = float(super().drive(distance))
        return distance

    def get_fare(self):
        fare = super().get_fare() + self.flagfall
        return fare
