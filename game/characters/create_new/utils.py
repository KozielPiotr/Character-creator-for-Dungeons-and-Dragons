"""Utilities for create new character"""


from time import sleep
import inspect

from game.utilities.utils import clear, spin
from game.throws.dice_throw import throw_dices


def choices_dict(module):
    """makes dictionary with all subclasses for race, class etc"""
    obj_list = [obj for elem, obj in inspect.getmembers(module) if inspect.isclass(obj) and obj.name != ""]
    obj_dict = {}
    number = 1
    for race in obj_list:
        obj_dict[number] = race
        number += 1
    return obj_dict


def header(chosen_race, chosen_class, chosen_name):
    """Prints header for character creator"""

    def choices(race, ch_class, name):
        """Prints user's choices"""

        if race or ch_class or name:
            print("\n\tYou are: ")
            if race:
                print("\t-race: {}".format(race.name))
            if ch_class:
                print("\t-class: {}".format(ch_class.name))
            if name:
                print("\t-name: {}".format(name))
            print("\n" + 80 * "#")

    clear()
    print(80*"#")
    print("#" + "#".rjust(79))
    print("#" + "CHARACTER CREATOR".center(78) + "#")
    print("#" + "#".rjust(79))
    print(80 * "#")
    choices(chosen_race, chosen_class, chosen_name)


def race_choose(races, chosen_race, chosen_class, chosen_name):
    """Player chooses character's race"""

    answer = False
    while answer is False:
        header(chosen_race, chosen_class, chosen_name)
        print("\n\tCHOOSE RACE:")
        for race_num in races:
            print("\t{}: {}".format(race_num, races[race_num].name))
        chosen_race_num = input("\nyour choice: ")
        try:
            if int(chosen_race_num) in races:
                return races[int(chosen_race_num)]
            header(chosen_race, chosen_class, chosen_name)
            print("\n\nchoose correct number")
            sleep(1)
        except ValueError:
            header(chosen_race, chosen_class, chosen_name)
            print("\n\nchoose correct number")
            sleep(1)


def class_choose(classes, chosen_race, chosen_class, chosen_name):
    """Player chooses character's class"""

    answer = False
    while answer is False:
        header(chosen_race, chosen_class, chosen_name)
        print("\n\tCHOOSE CLASS:")
        for class_num in classes:
            print("\t{}: {}".format(class_num, classes[class_num].name))
        chosen_class_num = input("\nyour choice: ")
        try:
            if int(chosen_class_num) in classes:
                return classes[int(chosen_class_num)]
            header(chosen_race, chosen_class, chosen_name)
            print("\n\nchoose correct number")
            sleep(1)
        except ValueError:
            header(chosen_race, chosen_class, chosen_name)
            print("\n\nchoose correct number")
            sleep(1)


def name_choose(chosen_race, chosen_class, chosen_name):
    """Player chooses character's name"""

    header(chosen_race, chosen_class, chosen_name)
    name = input("What is your name? ")
    return name


def confirm(races, chosen_race, chosen_class, chosen_name):
    """Player decides to accept choices or not"""

    confirmed = False
    while confirmed is False:
        header(chosen_race, chosen_class, chosen_name)
        ans = input("Confirm your choices?\n1. Yes\n2. No\n")
        if ans == "1":
            confirmed = True
        elif ans == "2":
            header(chosen_race, chosen_class, chosen_name)
            to_change = input("1. change race\n2. change class\n3. change name")
            if to_change == "1":
                chosen_race = race_choose(races, chosen_race, chosen_class, chosen_name)
            elif to_change == "2":
                chosen_class = class_choose(races, chosen_race, chosen_class, chosen_name)
            elif to_change == "3":
                chosen_name = name_choose(chosen_race, chosen_class, chosen_name)
            else:
                header(chosen_race, chosen_class, chosen_name)
                print("\n\nchoose correct number")
                sleep(1)
        else:
            header(chosen_race, chosen_class, chosen_name)
            print("\n\nchoose correct number")
            sleep(1)

    return {"confirmed": confirmed, "race": chosen_race, "class": chosen_class, "name": chosen_name}


def draw_attributes():
    """Throws 6 times 4 6-sided dices to draw attributes"""

    throws = []
    throw = 1
    while throw <= 6:
        throw_result = throw_dices(4, 6)
        throw_result.remove(min(throw_result))
        throws.append(sum(throw_result))
        throw += 1
    return throws


def distribute_attributes(new_character):
    """Allows the player to split values between attributes"""

    def set_attrib(attrib_name):
        """Sets chosen attribute"""

        corr_ans = False
        while corr_ans is False:
            header(new_character.race, new_character.character_class, new_character.name)
            print("\nDRAWN VALUES:")
            print(*values, sep="   ")
            chosen_val = input("CHOOSE VALUE FOR {}: ".format(attrib_name))
            if chosen_val.isnumeric() and int(chosen_val) in values:
                new_character.__dict__[attrib_name.lower()] += int(chosen_val)
                values.remove(int(chosen_val))
                corr_ans = True
            else:
                header(new_character.race, new_character.character_class, new_character.name)
                print("\n\nchoose correct number")
                sleep(1)

    character_attribs = ["STRENGTH", "CONSTITUTION", "DEXTERITY", "INTELLIGENCE", "WISDOM", "CHARISMA"]

    values = draw_attributes()
    header(new_character.race, new_character.character_class, new_character.name)
    print("THROWING DICES FOR ATTRIBUTES VALUES")
    spin(1.5)

    for attrib in character_attribs:
        set_attrib(attrib)
