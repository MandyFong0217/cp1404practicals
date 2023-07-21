"""
 CP1404
 test that the last two methods work as expected.
"""

from prac_06.guitar import Guitar

GibsonL_5 = Guitar('Gibson L-5 CES', 1022, 16035.40)
AnotherGuitar = Guitar('Another Guitar', 2013, 10000)

print(GibsonL_5.get_age())  # Expected 100. Got 100
print(AnotherGuitar.get_age())  # Expected 9. Got 9
print(GibsonL_5.is_vintage())  # Expected True. Got True
print(AnotherGuitar.is_vintage())
