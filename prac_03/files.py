"""Module docstring"""


# imports
# CONSTANTS

def main():
    """Function docstring"""
    # statements...
    total_for_all_lines()


def ask_name():
    """ask the name"""
    f = open('name.txt', 'w')
    name = input('Please enter your name:')
    f.write(name)
    f.write('\n')
    f.close()


def read_name():
    file = open('name.txt', 'r')
    name = file.read()
    print('Your name is ', name)


def add_first_two_numbers():
    number_file = open('number.txt', 'r')
    number = number_file.readlines()
    print(int(number[0]) + int(number[1]))


def total_for_all_lines():
    number_file = open('number.txt', 'r')
    number = number_file.readlines()
    result = 0
    for line in number:
        result = result + int(line)
    print(result)


main()
