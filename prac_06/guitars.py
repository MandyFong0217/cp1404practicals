"""
 CP1404
 Playing the Guitars
"""

from prac_06.guitar import Guitar

guitars = []
print('My guitars!')
name = input('Name: ')
while name != '':
    year = int(input('Year: '))
    cost = float(input('Cost: $'))
    print(f'{name} ({year}) : ${cost:.2f} added.')
    guitars.append(Guitar(name, year, cost))
    print('\n', end='')
    name = input('Name: ')

# guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

print('These are my guitars:')
for i, guitar in enumerate(guitars, 1):
    vintage_string = "" if not Guitar.is_vintage(guitar) else " (vintage)"
    # do something with i (the index) and guitar (the element)
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
