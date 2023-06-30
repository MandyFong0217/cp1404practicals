"""Module docstring"""


# imports
# CONSTANTS

def list_numbers():
    """Function docstring"""
    num_numbers = 5
    numbers = []
    for i in range(num_numbers):
        number = input('numbers:')
        numbers.append(int(number))
        if i == 0:
            first_number = number
        elif i == num_numbers - 1:
            last_number = number

    print('The first number is', first_number)
    print('The last number is', last_number)
    print('The smallest number is', min(numbers))
    print('The largest number is', max(numbers))
    print('The average of the numbers is', sum(numbers) / num_numbers)


def check_username():
    """Function docstring"""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    name = input('input username:')
    if name in usernames:
        print('Access granted')
    else:
        print('Access denied')


def main():
    list_numbers()
    check_username()


main()
