# pylint: disable=too-few-public-methods

"""
Classes for characters:
"""

from game.mechanics.throws import dice_throw


class CharacterClass:
    """Base class for every character class"""

    name = ""

    def __repr__(self):
        return "{}".format(self.name)


class Barbarian(CharacterClass):
    """Class for barbarian"""

    name = "barbarian"
    hp = 12
    hit_die = dice_throw.throw_dices(1, 12)


class Bard(CharacterClass):
    """Class for bard"""

    name = "bard"
    hp = 6
    hit_die = dice_throw.throw_dices(1, 6)


class Cleric(CharacterClass):
    """Class for cleric"""

    name = "cleric"
    hp = 8
    hit_die = dice_throw.throw_dices(1, 8)


class Druid(CharacterClass):
    """Class for druid"""

    name = "druid"
    hp = 8
    hit_die = dice_throw.throw_dices(1, 8)


class FighterClass(CharacterClass):
    """Class for warrior"""

    name = "fighter"
    hp = 10
    hit_die = dice_throw.throw_dices(1, 10)


class Monk(CharacterClass):
    """Class for monk"""

    name = "monk"
    hp = 8
    hit_die = dice_throw.throw_dices(1, 8)


class Paladin(CharacterClass):
    """Class for paladin"""

    name = "paladin"
    hp = 10
    hit_die = dice_throw.throw_dices(1, 10)


class Psion(CharacterClass):
    """Class for psion"""

    name = "psion"
    hp = 4
    hit_die = dice_throw.throw_dices(1, 4)


class PsychicWarrior(CharacterClass):
    """Class for psychic warrior"""

    name = "psychic warrior"
    hp = 8
    hit_die = dice_throw.throw_dices(1, 8)


class Ranger(CharacterClass):
    """Class for psychic ranger"""

    name = "ranger"
    hp = 8
    hit_die = dice_throw.throw_dices(1, 8)


class Rogue(CharacterClass):
    """Class for psychic rogue"""

    name = "rogue"
    hp = 6
    hit_die = dice_throw.throw_dices(1, 6)


class Sorcerer(CharacterClass):
    """Class for sorcerer"""

    name = "sorcerer"
    hp = 4
    hit_die = dice_throw.throw_dices(1, 4)


class Soulknife(CharacterClass):
    """Class for soulknife"""

    name = "soulknife"
    hp = 10
    hit_die = dice_throw.throw_dices(1, 10)


class Wilder(CharacterClass):
    """Class for wilder"""

    name = "wilder"
    hp = 6
    hit_die = dice_throw.throw_dices(1, 6)


class Wizard(CharacterClass):
    """Class for wizard"""

    name = "wizard"
    hp = 4
    hit_die = dice_throw.throw_dices(1, 4)
