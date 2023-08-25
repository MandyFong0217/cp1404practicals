"""
CP1404 Practical
lets the user enter and clear their name, and greets them when we press a button
Estimate time: 30min
Actual time: 20min
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        print("test")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def clear_button(self):
        print("clear")
        self.root.ids.output_label.text = ''
        self.root.ids.input_name.text = ''


# Create and start the App running
BoxLayoutDemo().run()
