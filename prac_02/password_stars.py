"""
password stars
"""


def main():
    mini_length_password = 10
    password = get_password(mini_length_password)
    print_star(password)


def print_star(password):
    """print asterisks as long as the word"""
    for i in range(len(password)):
        print("*", end='')


def get_password(mini_length_password):
    """get and check the password"""
    password = input("Input password:")
    while len(password) < mini_length_password:
        print("Invalid Password")
        password = input("Input again:")
    return password


main()
