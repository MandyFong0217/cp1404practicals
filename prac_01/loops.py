for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a
for i in range(0, 100, 10):
    print(i, end=' ')
print()

# b
for i in range(0, 20, 1):
    print(20 - i, end=' ')
print()

# c
num_stars = int(input("Number of stars:"))
for i in range(num_stars):
    print("*", end='')
print()

num_stars = int(input("Number of stars:"))
for i in range(num_stars + 1):
    print("*" * i)
