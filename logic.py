import enum


class Color(enum.Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'
    YELLOW = 'yellow'


class Person:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    @staticmethod
    def term(plyer_li, pvi_p=None):
        if pvi_p:
            try:
                return plyer_li[plyer_li.index(pvi_p)+1]
            except IndexError:
                return plyer_li[0]
        else:
            return plyer_li[0]


class Bead:
    def __init__(self, color, number, postion=None, in_game=False, in_home=False):
        self.color = color
        self.number = number
        self.postion = postion
        self.in_game = in_game
        self.in_home = in_home

    @staticmethod
    def creat_beads(color):
        return [Bead(color, i) for i in range(1, 5)]


