"""Creates new character"""

from game.characters.characters_clss import Character
from game.races import races_clss
from game.classes import classes_clss
from game.characters.create_new.utils import choices_dict, race_choose, class_choose, name_choose, confirm,\
    distribute_attributes


def character_creator():
    """Player creates new character here"""
    races = choices_dict(races_clss)
    classes = choices_dict(classes_clss)

    chosen_race = None
    chosen_class = None
    chosen_name = None

    chosen_race = race_choose(races, chosen_race, chosen_class, chosen_name)
    chosen_class = class_choose(classes, chosen_race, chosen_class, chosen_name)
    chosen_name = name_choose(chosen_race, chosen_class, chosen_name)

    char = confirm(races, classes, chosen_race, chosen_class, chosen_name)
    if char["confirmed"] is True:
        new_character = Character(char["race"], char["class"], char["name"])

        distribute_attributes(new_character)

        print("\n\nname: ", new_character.name)

        print("\nstrength: ", new_character.strength)
        print("constitution: ", new_character.constitution)
        print("dexterity: ", new_character.dexterity)
        print("intelligence: ", new_character.intelligence)
        print("wisdom: ", new_character.wisdom)
        print("charisma: ", new_character.charisma)

        return new_character

    return None
