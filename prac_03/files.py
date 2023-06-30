"""Demonstration of file usage"""


# imports
# CONSTANTS

def main():
    """Function docstring"""
    # statements...
    get_name()
    read_name()
    add_first_two_numbers()
    total_for_all_lines()


# 1
def get_name():
    """ask the name"""
    f = open('name.txt', 'w')
    name = input('Please enter your name:')
    f.write(name)
    f.write('\n')
    f.close()


# 2
def read_name():
    file = open('name.txt', 'r')
    name = file.read()
    print('Your name is ', name)


# 3
def add_first_two_numbers():
    number_file = open('number.txt', 'r')
    number = number_file.readlines()
    print(int(number[0]) + int(number[1]))


# 4
def total_for_all_lines():
    number_file = open('number.txt', 'r')
    number = number_file.readlines()
    result = 0
    for line in number:
        result = result + int(line)
    print(result)


main()
