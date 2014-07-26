__author__ = 'drew'


from desert import Desert
from forest import Forest
from plains import Plains
from water import Water
from random import randrange



def generate_random_tile():
    choice = randrange(4)
    return {
        0 : Desert(),
        1 : Forest(),
        2 : Plains(),
        3 : Water()
    }[choice]