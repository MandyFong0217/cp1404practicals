"""Module docstring"""
import random


# imports
# CONSTANTS

def main():
    """Function docstring"""
    # statements...
    CONSTANTS = []
    line = []
    num_line = int(input('How many quick picks? '))
    for i in range(num_line):
        for x in range(6):
            random_num = random.randrange(1, 45)
            while random_num in line:
                random_num = random.randrange(1, 45)
            line.append(random_num)

            if x == 5:
                CONSTANTS.append(line)
                CONSTANTS[i].sort()
                line = []

    for i in range(num_line):
        for x in range(6):
            print("{:2}".format(CONSTANTS[i][x]), end=' ')
            if x == 5:
                print('\n', end='')


def do_stuff():
    """Function docstring"""
    # statements...


main()
