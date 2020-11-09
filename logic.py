import enum


class Person:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    @staticmethod
    def term(plyer_li,pvi_p=None):
        if pvi_p:
            return plyer_li[plyer_li.index(pvi_p)+1]
        else:
            return plyer_li[0]




class Bead:
    def __init__(self, owner, number, postion=None, in_game=False, in_home=False):
        self.owner = owner
        self.number = number
        self.postion = postion
        self.in_game = in_game
        self.in_home = in_home

    @staticmethod
    def creat_beads(color):
        if color == 'red':
            mohre1_red = Bead('red', 1)
            mohre2_red = Bead('red', 2)
            mohre3_red = Bead('red', 3)
            mohre4_red = Bead('red', 4)
            return [mohre1_red, mohre2_red, mohre3_red, mohre4_red]

        if color == 'blue':
            mohre1_blue = Bead('blue', 1)
            mohre2_blue = Bead('blue', 2)
            mohre3_blue = Bead('blue', 3)
            mohre4_blue = Bead('blue', 4)
            return [mohre1_blue, mohre2_blue, mohre3_blue, mohre4_blue]

        if color == 'green':
            mohre1_green = Bead('green', 1)
            mohre2_green = Bead('green', 2)
            mohre3_green = Bead('green', 3)
            mohre4_green = Bead('green', 4)
            return [mohre1_green, mohre2_green, mohre3_green, mohre4_green]

        if color == 'yellow':
            mohre1_yellow = Bead('yellow', 1)
            mohre2_yellow = Bead('yellow', 2)
            mohre3_yellow = Bead('yellow', 3)
            mohre4_yellow = Bead('yellow', 4)
            return [mohre1_yellow, mohre2_yellow, mohre3_yellow, mohre4_yellow]

