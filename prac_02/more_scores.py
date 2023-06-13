import random


def check_valid(score):
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Input a valid score:"))
    return score


def get_result(score):
    if score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    elif score >= 0:
        return "Bad"


def display_menu():
    print("(E)nter a number of scores \n(G)enerate random numbers (scores) "
          "\n(W)rite the 'result' to a file \n(Q)uit")  # display menu


def main():
    score = []
    f = open('result.txt', 'w')
    display_menu()
    choice = input()

    while choice != "Q":
        if choice == "E":
            score.append(int(check_valid(float(input("Enter a number of scores:")))))
            display_menu()  # display menu
            choice = input()  # get choice

        elif choice == "G":
            random_score = random.randrange(0, 100)
            score.append(random_score)
            print("The random score is ", random_score)
            display_menu()  # display menu
            choice = input()  # get choice

        elif choice == "W":
            write_file(f, score)
            display_menu()  # display menu
            choice = input()  # get choice
        else:
            print("Invalid choice")  # display invalid message
            display_menu()  # display menu
            choice = input()  # get choice
    print("Thank you!")


def write_file(f, score):
    for result in score:
        line = '%s is %s' % (result, get_result(float(result)))
        print(line)
        f.write(line)
        f.write('\n')


main()
