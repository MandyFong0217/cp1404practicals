"""
CP1404 - band class
Estimate time: 30min
Actual time: 30min
"""


class Band:

    def __init__(self, name=""):
        self.name = name
        self.musicians = []

    def __str__(self):
        musicians_str = ', '.join([str(musician) for musician in self.musicians])
        return f'{self.name} ({musicians_str})'

    def __repr__(self):
        return str(vars(self))

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        play_str = []
        for musician in self.musicians:
            if not musician.instruments:
                play_str.append(f'{self.name} needs an instrument!')
            else:
                play_str.append(f"{self.name} is playing: {musician.instruments[0]}")
        return '\n'.join(play_str)
