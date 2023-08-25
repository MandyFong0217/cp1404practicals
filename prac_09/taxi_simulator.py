"""
CP1404 -
Write a taxi simulator program that uses your Taxi and SilverServiceTaxi classes.
Estimate time: 1hour
Actual time: 1.5hr
"""
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill = 0
    current_taxi = None
    print("Let's drive!")
    display_menu()
    choice = str(input(">>> ")).lower()
    while choice != 'q':
        if choice == 'd':
            if current_taxi is None:
                print('You need to choose a taxi before you can drive')
            else:
                drive_distance = int(input('Drive how far? '))
                taxis[current_taxi].drive(drive_distance)
                bill += taxis[current_taxi].get_fare()
                print(f'Your Prius trip cost you ${taxis[current_taxi].get_fare():.2f}')
        elif choice == 'c':
            print('Taxis available: ')
            for i, taxi in enumerate(taxis):
                print(f'{i} - {taxi}')
            current_taxi = int(input('Choose taxi: '))
            if current_taxi < 0 or current_taxi > len(taxis) - 1:
                print('Invalid taxi choice')
        else:
            print('Invalid option')
        print(f'Bill to date: ${bill:.2f}')
        display_menu()
        choice = str(input(">>> ")).lower()
    print(f'Total trip cost: ${bill:.2f}')
    print('Taxis are now:')
    for i, taxi in enumerate(taxis):
        print(f'{i} - {taxi}')


def display_menu():
    print('q)uit, c)hoose taxi, d)rive')


main()
