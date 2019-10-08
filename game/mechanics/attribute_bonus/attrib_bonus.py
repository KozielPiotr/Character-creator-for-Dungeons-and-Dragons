"""Count attribute bonus"""


def count_att_bonus(att):
    """Counts bonus given by attribute"""

    bonus = -5
    if att == 1:
        return bonus

    for val in range(2, 101, 2):
        bonus += 1
        if att in range(val, val+2):
            return bonus
    return None
