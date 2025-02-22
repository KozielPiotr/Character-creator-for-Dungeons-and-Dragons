# pylint: disable=too-few-public-methods
"""
Classes for races
"""


class Race:
    """Base class for every character race"""

    name = ""

    strength = 0
    constitution = 0
    dexterity = 0
    intelligence = 0
    wisdom = 0
    charisma = 0

    size = "medium"

    def __repr__(self):
        return "{}".format(self.name)


class Human(Race):
    """Class for human"""

    name = "human"

    size = "medium"


class Elf(Race):
    """Class for elf"""

    name = "elf"

    dexterity = 2
    constitution = -2

    size = "medium"


class Gnome(Race):
    """Class for gnome"""

    name = "gnome"

    strength = -2
    constitution = 2

    size = "small"


class Dwarf(Race):
    """Class for dwarfs"""

    name = "dwarf"

    constitution = 2
    charisma = -2

    size = "medium"


class Halfling(Race):
    """Class for halfling"""

    name = "halfling"

    strength = -2
    dexterity = 2

    size = "small"


class HalfElf(Race):
    """Class for half-elf"""

    name = "half-elf"

    size = "medium"


class HalfOrc(Race):
    """Class for half-orc"""

    name = "half-orc"

    strength = 2
    intelligence = -2
    charisma = -2

    size = "medium"
