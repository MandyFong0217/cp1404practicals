"""
CP1404/CP5632 Practical
Miles to Kilometres Converter
Estimate time: 30min
Actual time: 20min
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KILOMETRES = 0.621371


def validate_miles(value):
    """change value to 0.0 when nothing in the text box"""
    try:
        miles = float(value)
    except ValueError:
        miles = 0.0
    return miles


class MilesToKilometresConverter(App):
    """ Miles to Kilometres Converter """
    message = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (200, 100)
        self.title = "Miles to Kilometres Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        result = validate_miles(value) / MILES_TO_KILOMETRES
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment):
        result = int(validate_miles(self.root.ids.input_number.text)) + int(increment)
        self.root.ids.input_number.text = str(result)
        self.handle_calculate(result)


MilesToKilometresConverter().run()
