# pylint: disable=too-few-public-methods

"""
Classes for characters
"""


class Character:
    """Base class for every character"""

    def __init__(self, race, ch_class, name):
        self.race = race
        self.character_class = ch_class
        self.level = 1
        self.name = name

        self.strength = race.strength
        self.constitution = race.constitution
        self.dexterity = race.dexterity
        self.intelligence = race.intelligence
        self.wisdom = race.wisdom
        self.charisma = race.charisma

    def __repr__(self):
        return "{}".format(self.name)
