import sys
import random


def _set_hp():
    base_hp = 7
    added_hp = random.randint(0, 4)
    return base_hp + added_hp


def _set_atk():
    base_atk = 2
    added_atk = random.randint(0, 2)
    return base_atk + added_atk


class Cat:

    def __init__(
            self,
            name,
            location
    ):
        self.name = name
        self.location = location
        self.alive = True
        self.tame = False
        self.HP = _set_hp()
        self.ATK = _set_atk()

        self.possible_positions = ['visible', 'under_feet', 'hiding', 'having_the_high_ground', 'on_player']
        self.body_positions = ['sitting', 'loafing', 'walking', 'running',
                               'crawling', 'climbing', 'jumping', 'crouching', 'lying']
        self.movement_speed = ['idle', 'slow', 'fast', 'i_am_speed']

    def tame(self):
        # NOTE: add conditions
        self.tame = True


sys.exit()