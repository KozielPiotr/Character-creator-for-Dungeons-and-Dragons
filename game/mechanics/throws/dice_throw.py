"""Throws n-number of n-sided dices"""

from random import randint


def throw_dices(dices, sides):
    """
    Throw given number of seleted-sided dices
    :param dices: number of dices
    :param sides: number of sides of dices
    :return: list of every dice result
    """
    throw = []
    dice = 1
    while dice <= dices:
        throw.append(randint(1, sides))
        dice += 1

    return throw
