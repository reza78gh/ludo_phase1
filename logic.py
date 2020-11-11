import enum


class Color(enum.Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'
    YELLOW = 'yellow'


class Person:
    term = None
    
    def __init__(self, name, color):
        self.name = name
        self.color = color

    @staticmethod
    def next_term(plyer_li):
        if Person.term:
            try:
                Person.term = plyer_li[plyer_li.index(Person.term)+1]
            except IndexError:
                Person.term = plyer_li[0]
        else:
            Person.term = plyer_li[0]



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


# todo: only one obj
class Base:
    base = []
    li_out = []
    li_in_home = []

    @staticmethod
    def creat_base(*args):
        Base.base = ['e' for _ in range(24)]
        for li in args:
            for obj in li:
                if isinstance(obj, Bead):
                    Base.li_out.append(obj)
                else:
                    raise Exception('obj not in class Bead')
        print(args)
        #return base 
        
    @staticmethod
    def check_place(place):
        return Base.base[place]

    def set_posation(self,posation,target_bead=None):
        if target_bead:
            Base.li_out.append(target_bead)
        Base[posation]=self
        