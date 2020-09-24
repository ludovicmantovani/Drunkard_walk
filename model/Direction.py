from enum import Enum, auto
from random import choice


def get_random_direction():
    directions = [direction for direction in DirectionType]
    return choice(directions)


class DirectionType(Enum):
    UP = auto()
    DOWN = auto()
    RIGHT = auto()
    LEFT = auto()


