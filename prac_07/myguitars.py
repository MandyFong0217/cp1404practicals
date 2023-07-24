"""
CP1404/CP5632 Practical
Write a program to read all of these guitars and store them in a list of Guitar objects,
 using the class that you wrote recently
"""

from prac_06.guitar import Guitar


def main():
    guitars = []
    # Open the file for reading
    in_file = open('guitars.csv', 'r')
    # File format is like: Language,Typing,Reflection,Year
    # 'Consume' the first line (header) - we don't need its contents
    in_file.readline()
    # All other lines are language data
    for line in in_file:
        # print(repr(line))  # debugging
        # Strip newline from end and split it into parts (CSV)
        parts = line.strip().split(',')
        # print(parts)  # debugging
        # Reflection is stored as a string (Yes/No) and we want a Boolean
        # Reflection is stored as a string (Yes/No) and we want a Bool
        # Construct a ProgrammingLanguage object using the elements
        # year should be an int
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        # Add the language we've just constructed to the list
        guitars.append(guitar)
    # Close the file as soon as we've finished reading it
    in_file.close()
    guitars = sorted(guitars)
    for guitar in guitars:
        print(guitar)




main()
