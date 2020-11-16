import enum

class Color(enum.Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'
    YELLOW = 'yellow'


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
        print('what the fuck: ',self.postion,win_place)
        
        if 0 < win_place - self.postion <= 6:
            if self.postion + roll -1 < win_place:
                return 'move'
            elif self.postion + roll -1 == win_place:
                return 'win'
            else:
                return 'stop'

    @staticmethod
    def creat_beads(color):
        return [Bead(color, i) for i in range(1, 5)]


# todo: only one obj
class Base:
    red_win = 6
    blue_win = 24
    green_win = 30
    yellow_win = 40
    red_start = 7
    blue_start = 1
    green_start = 13
    yellow_start = 19
    base = []
    li_out = []
    li_in_home = []
    in_home_blue = []
    in_home_red = []

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
        return Base.base[int(place-1)]

    def set_posation(self,posation,target_bead=None):
        if target_bead:
            Base.li_out.append(target_bead)
        Base.base[posation-1]=self
        self.postion = posation
        

Base.creat_base()
rb = Bead.creat_beads('red')
bb = Bead.creat_beads('blue')
ali = Person('ali','red')
reza = Person('reza','blue')
Person.player_li = [reza, ali]
Person.next_turn()
Base.in_home_blue = bb
Base.in_home_red = rb
# print(Person.turn.color)
# print(Base.in_home_blue)
# print(Color.GREEN)
