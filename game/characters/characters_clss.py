# pylint: disable=too-few-public-methods

"""
Classes for characters
"""


from game.mechanics.attribute_bonus.attrib_bonus import count_att_bonus


class Character:
    """Base class for every character"""

    hp = 0

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

    def count_hp(self):
        """Counts how much HP character will have after creation"""
        print(self.character_class.hp, count_att_bonus(self.constitution))
        return self.character_class.hp + count_att_bonus(self.constitution)

    def __repr__(self):
        return "{}".format(self.name)
