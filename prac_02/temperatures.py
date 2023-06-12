"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def Celsius_to_Fahtenheit():
    "Convert Celsius to Fahrenheit"
    global fahrenheit
    fahrenheit = celsius * 9.0 / 5 + 32


def Fahrenheit_to_Celsius():
    "Convert Fahrenheit to Celsius"
    global celsius
    celsius = 5 / 9 * (fahrenheit - 32)


while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        Celsius_to_Fahtenheit()
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        Fahrenheit_to_Celsius()
        print(f"Result: {celsius:.2f} F")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")