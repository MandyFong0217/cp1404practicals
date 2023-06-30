"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ")
# 3.make lowercase inputs also work
state_code = state_code.upper()
while state_code != "":
    # 5.change to Easier to Ask Forgiveness than Permission approach
    try:
        CODE_TO_NAME[state_code]
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ")
    state_code = state_code.upper()

# 4.print all the states
for short_name in CODE_TO_NAME:
    print('{:3} is {}'.format(short_name, CODE_TO_NAME[short_name]))
