"""
score menu
"""


def main():
    """Function docstring"""
    # statements...
    score = 0
    display_menu()
    choice = input("Your choice:")  # get choice
    while choice.upper() != "Q":
        if choice.upper() == "G":
            "Get a valid score (must be 0-100 inclusive)"
            score = int(input("Input a valid score:"))
            score = check_valid(score)
            display_menu()
            choice = input("Your choice:")  # get choice
        elif choice.upper() == "P":
            "Print result"
            print(get_result(score))
            display_menu()
            choice = input("Your choice:")  # get choice
        elif choice.upper() == "S":
            "Show stars (this should print as many stars as the score)"
            print_stars(score)
            display_menu()
            choice = input("Your choice:")  # get choice
        else:
            print("Invalid choice")  # display invalid message
            display_menu()  # display menu
            choice = input("Your choice:")  # get choice
    print("Goodbye!")  # display finished message


def print_stars(score):
    for i in range(score):
        print("*", end='')
    print("")


def get_result(score):
    if score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    elif score >= 0:
        return "Bad"


def check_valid(score):
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Input a valid score:"))
    return score


def display_menu():
    print(
        "(G)et a valid score (must be 0-100 inclusive)\n"
        "(P)rint result (copy or import your function to determine the result from score.py)"
        "\n(S)how stars (this should print as many stars as the score)\n(Q)uit")  # display menu


main()
