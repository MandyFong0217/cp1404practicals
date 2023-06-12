"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    """determine score status"""
    score = float(input("Enter Score: "))
    print(return_score_status(score))
    random_score = random.randrange(0,100)
    print("random_score:", random_score)
    print(return_score_status(random_score))


def return_score_status(score):
    if score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    elif score >= 0:
        return "Bad"
    else:
        return "Invalid score"


main()


def check_valid(score):
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Input a valid score:"))
    return score