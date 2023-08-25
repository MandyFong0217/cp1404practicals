"""
CP1404
silver service taxi class test
Estimate time: 1hr
Actual time: 1hr
"""
from prac_09.silver_service_taxi import SilverServiceTaxi

trip = SilverServiceTaxi('Hummer', 200, 2)
trip.drive(18)
print(trip)
# test code.the fare should be $48.78
print(f'${trip.get_fare():.2f}')
