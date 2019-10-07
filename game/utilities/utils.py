"""Utilities for whole project"""

from os import system, name
from itertools import cycle
from time import sleep


def clear():
    """Clears console window"""

    if name == 'nt':
        system('cls')
    else:
        system('clear')


def spin(duration):
    """Creates spinning effect dor given duration"""
    e_time = 0
    for frame in cycle(r"-\|/-\|/"):
        print("\r", frame, sep="", end="", flush=True)
        sleep(0.2)
        e_time += 0.2
        if e_time > duration:
            break
