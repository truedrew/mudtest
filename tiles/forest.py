__author__ = 'drew'

from random import randrange
from bottle import template

class Forest:
    def __init__(self):
        self.type = "forest"
        self.color = "#336600"
        self.commands = ["Harvest Lumber"]
        self.trees = randrange(10) * 10
