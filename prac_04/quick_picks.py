"""
"Quick Pick" Lottery Ticket Generator
"""
import random


def main():
    num_line = int(input('How many quick picks? '))
    CONSTANTS = created_constants_list(num_line)
    print_result(CONSTANTS, num_line)


def print_result(CONSTANTS, num_line):
    """This function print the Quick Pick Lottery Ticket Generator"""
    for i in range(num_line):
        for x in range(6):
            # format the printing
            print("{:2}".format(CONSTANTS[i][x]), end=' ')
            if x == 5:
                print('\n', end='')


def created_constants_list(num_line):
    """This function created a list of constants"""
    line = []
    CONSTANTS = []
    for i in range(num_line):
        for x in range(6):
            random_num = random.randrange(1, 45)
            # check the number is not repeated in the line
            while random_num in line:
                random_num = random.randrange(1, 45)
            line.append(random_num)

            if x == 5:
                CONSTANTS.append(line)
                # sorted the line
                CONSTANTS[i].sort()
                line = []
    return CONSTANTS


main()
