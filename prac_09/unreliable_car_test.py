""""
CP1404
test unreliable car class
Estimate time: 20min
Actual time: 20min
"""
from prac_09.unreliable_car import UnreliableCar

# Create a new object
my_taxi = UnreliableCar('Prius 1', 100, 50)

# Drive 40 km
my_taxi.drive(30)

# Display my_taxi detail and current fare
print(my_taxi)