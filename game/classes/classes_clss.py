# pylint: disable=too-few-public-methods

"""
Classes for characters:
"""

from random import randint


class CharacterClass:
    """Base class for every character class"""

    name = ""

    def __repr__(self):
        return "{}".format(self.name)


class FighterClass(CharacterClass):
    """class for warrior"""

    name = "fighter"
    endurance_throw = randint(1, 10)
