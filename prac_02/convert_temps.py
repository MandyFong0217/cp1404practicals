"""""
More temperatures
"""""


def main():
    input_file = open("temps_input.txt", 'r')
    output_file = open("temps_output.txt", 'w')
    data = input_file.read()
    list_data = [float(n) for n in data.split('\n') if is_float(n)]
    print(list_data)
    print(len(list_data))

    for i in range(len(list_data)):
        celsius = fahrenheit_to_celsius(list_data[i])
        output_file.write(str(celsius))
        output_file.write('\n')


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def is_float(n):
    try:
        float(n)
        return True
    except:
        return False


main()
