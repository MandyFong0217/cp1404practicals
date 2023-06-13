"""""
More temperatures
simulates a population of gophers over a ten-year period
"""""
import random


def main():
    print("Welcome to the Gopher Population Simulator!\nStarting population: 1000\nYear 1\n")
    population = 1000
    period = 10
    for year in range(2, period+1):
        born_number = int(population*(random.randrange(10, 20)/100))
        die_number = int(population*(random.randrange(5, 25)/100))
        print('%s gophers were born. %s died.' % (born_number, die_number))
        population = population + born_number - die_number
        print('Population:', population)
        print('Year ', year)
        print('\n')


main()
