"""
Display random numbers
"""
import random

RANDOM_NUMBERS = []
MIN_RANGE = 1  # min number should be 1
MAX_RANGE = 45  # max number should be 45

quick_pick = int(input("How many quick picks? "))

for count in range(quick_pick):
    for i in range(6):
        number = random.randint(MIN_RANGE, MAX_RANGE)
        while number in RANDOM_NUMBERS:
            number = random.randint(MIN_RANGE, MAX_RANGE)
        RANDOM_NUMBERS.append(number)
    RANDOM_NUMBERS = [str(number) for number in RANDOM_NUMBERS]
    print(" ".join(sorted(f'{number:>2}' for number in RANDOM_NUMBERS)))
    RANDOM_NUMBERS = []
