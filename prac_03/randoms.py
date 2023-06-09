"""
CP1404/CP5632 - Practical
Random Numbers
"""

import random


def main():
    print(random.randint(5, 20))  # line 1
    print(random.randrange(3, 10, 2))  # line 2
    print(random.uniform(2.5, 5.5))  # line 3

    # What did you see on line 1? 5
    # What was the smallest number you could have seen, what was the largest?5,20

    # What did you see on line 2?3 What was the smallest number you could have seen, what was the largest?3,9
    # Could line 2 have produced a 4?no because the program Returns any random integer from 3 to 10 with step 2.it
    # will be 3,5,7,9

    # What did you see on line 3?3.833085658945019
    # What was the smallest number you could have seen, what was the largest?2.5,5.5

    # Write code, not a comment, to produce a random number between 1 and 100 inclusive.
    print(random.randint(1, 100))


main()
