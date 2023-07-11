"""
look up hexadecimal colour codes
"""


def main():
    COLOUR_TO_CODE = {
        "eggplant": "#614051", "eggshell": "#f0ead6", "egyptian blue": "#1034a6",
        "electric blue": "#7df9ff", "aliceblue": "#f0f8ff", "aquamarine1": "#7fffd4",
        "aureolin": "#fdee00", "beaver": "#9f8170", "baby pink": "#f4c2c2", "black": "#000000"
    }

    colour_name = input("Enter the name of colour: ")
    # 3.make lowercase inputs also work
    colour_name = colour_name.lower()
    while colour_name != "":
        # 5.chane to Easier to Ask Forgiveness than Permission approach
        try:
            print(COLOUR_TO_CODE[colour_name])
        except KeyError:
            print("Invalid short state")
        colour_name = input("Enter the name of colour: ")
        colour_name = colour_name.lower()


main()
