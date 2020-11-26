class Person:
    turn = None
    player_li = []
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
        Person.player_li.append(self)

    @staticmethod
    def next_turn():
        if Person.turn:
            try:
                Person.turn = Person.player_li[Person.player_li.index(Person.turn)+1]
            except IndexError:
                Person.turn = Person.player_li[0]
        else:
            Person.turn = Person.player_li[0]



class Bead:
    def __init__(self, color, number, postion=None, in_game=False, in_home=False):
        self.color = color
        self.number = number
        self.postion = postion
        self.in_game = in_game
        self.in_home = in_home


    def check_win(self,roll):
        color = self.color
        if color == 'red':
            win_place = Base.red_win
        elif color == 'blue':
            win_place = Base.blue_win
        elif color == 'green':
            win_place = Base.green_win
        elif color == 'yellow':
            win_place = Base.yellow_win
        
        if 0 <= win_place - self.postion <= 6:
            if self.postion + roll -1 < win_place:
                return 'move'
            elif self.postion + roll -1 == win_place:
                return 'win'
            else:
                return 'stop'
        else:
            return 'move'

    @staticmethod
    def creat_beads(color):
        return [Bead(color, i) for i in range(1, 5)]


class Base:
    red_win = 6
    blue_win = 24
    green_win = 12
    yellow_win = 18
    red_start = 7
    blue_start = 1
    green_start = 13
    yellow_start = 19
    base = []
    out_blue = []
    out_red = []
    out_green = []
    out_yellow = []

    in_home_blue = []
    in_home_red = []
    in_home_green = []
    in_home_yellow = []

    @staticmethod
    def creat_base(*args):
        Base.base = ['e' for _ in range(24)]
        
    @staticmethod
    def check_place(place):
        return Base.base[int(place-1)]

    def set_posation(self,posation,target_bead=None):
        if target_bead:
            color = target_bead.color
            if color == 'blue':
                Base.out_blue.append(target_bead)
            if color == 'red':
                Base.out_red.append(target_bead)
            if color == 'green':
                Base.out_green.append(target_bead)
            if color == 'yellow':
                Base.out_yellow.append(target_bead)
        Base.base[posation-1]=self
        self.postion = posation

    @staticmethod
    def get_list(color,type_list):
        if color == 'blue':
            if type_list == 'out':
                return Base.out_blue
            elif type_list == 'home':
                return Base.in_home_blue
        elif color == 'red':
            if type_list == 'out':
                return Base.out_red
            elif type_list == 'home':
                return Base.in_home_red
        elif color == 'green':
            if type_list == 'out':
                return Base.out_green
            elif type_list == 'home':
                return Base.in_home_green
        elif color == 'yellow':
            if type_list == 'out':
                return Base.out_yellow
            elif type_list == 'home':
                return Base.in_home_yellow
        


def set_player(name,color):
    Person(name,color)
    list_beads = Base.get_list(color,'out') 
    beads = Bead.creat_beads(color)
    for bead in beads: list_beads.append(bead)

