"""
Basic list operations
&
Woefully inadequate security checker
"""


def list_numbers():
    """Basic list operations"""
    # This function list first,last,smallest,largest,average number
    num_numbers = 5
    numbers = []
    first_number = ''
    last_number = ''
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
    # This function check the username input that is valid or not
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
