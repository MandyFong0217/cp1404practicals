"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    for i in range(len(data)):
        print(f"{data[i][0]} is taught by {data[i][1]} and has {data[i][2]} students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    lines = input_file.readlines()
    for line in lines:
        line = line.split(',')
        line[2] = line[2].rstrip()
        data.append(line)
    input_file.close()
    return data


main()
