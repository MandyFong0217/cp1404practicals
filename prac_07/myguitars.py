"""
CP1404/CP5632 Practical
Write a program to read all of these guitars and store them in a list of Guitar objects,
 using the class that you wrote recently
"""

from prac_06.guitar import Guitar


def main():
    guitars = []
    # Open the file for reading
    in_file = open('guitars.csv', 'r+')
    # File format is like: Language,Typing,Reflection,Year
    # 'Consume' the first line (header) - we don't need its contents
    data = in_file.readlines()
    print(data)
    for line in data:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    guitars = sorted(guitars)
    for guitar in guitars:
        print(guitar)
    print('\n')
    print('My guitars!')
    name = input('Name: ')
    while name != '':
        year = int(input('Year: '))
        cost = float(input('Cost: $'))
        print(f'{name} ({year}) : ${cost:.2f} added.')
        guitar = Guitar(name, int(year), float(cost))
        guitars.append(guitar)
        print('\n', end='')
        name = input('Name: ')
    in_file.seek(0)
    for guitar in guitars:
        in_file.write(f'{guitar.name},{guitar.year},{guitar.cost}')
        in_file.write('\n')
    in_file.close()


main()
