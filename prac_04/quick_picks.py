"""
Display random numbers
"""
import random

RANDOM_NUMBERS = []

quick_pick = int(input("How many quick picks? "))

for count in range(quick_pick):
    for i in range(6):
        number = random.randint(1, 45)
        while number in RANDOM_NUMBERS:
            number = random.randint(1, 45)
        RANDOM_NUMBERS.append(number)
    RANDOM_NUMBERS = [str(number) for number in RANDOM_NUMBERS]
    print(" ".join(sorted(f'{number:>2}' for number in RANDOM_NUMBERS)))
    RANDOM_NUMBERS = []