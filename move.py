from logic import Base ,Bead, Person

# todo: check win
def check_move(place,roll):
    print('place clicked: ',place)
    # Person.next_turn() for all
    if place > 24 :
        if place == 25:
            print('here 24')
            li = Base.in_home_blue
            if li and Person.turn.color == 'blue':
                bead = li[0]
                target = Base.check_place(Base.blue_start)
                if target != 'e':
                    if bead.color == target.color:
                        return 'stop'
                    else:
                        Base.set_posation(bead,Base.blue_start,target)
                        li.remove(li[0])
                        Person.next_turn()
                        return f'move blue {Base.blue_start} l'
                Base.set_posation(bead,Base.blue_start)
                li.remove(li[0])
                Person.next_turn()
                return f'move blue {Base.blue_start} l'
            else:
                return 'stop'

        elif place == 26:
            li = Base.in_home_red
            if li and Person.turn.color == 'red':
                bead = li[0]
                target = Base.check_place(Base.blue_start)
                if target != 'e':
                    if bead.color == target.color:
                        return 'stop'
                    else:
                        Base.set_posation(bead,Base.red_start,target)
                        li.remove(li[0])
                        Person.next_turn()
                        return f'move red {Base.red_start} l'
                Base.set_posation(bead,Base.red_start)
                li.remove(li[0])
                Person.next_turn()
                return f'move red {Base.red_start} l'
            else:
                'stop'

        if place == 27:
            li = Base.in_home_green
            if li:
                bead = li[0]
                target = Base.check_place(Base.yellow_start)
                if target != 'e':
                    if bead.color == target.color:
                        return 'stop'
                    else:
                        Base.set_posation(bead,Base.green_start,target)
                        li.remove(li[0])
                        return 'move','green',Base.green_start
                Base.set_posation(bead,Base.green_start)
                li.remove(li[0])
                return 'move','green',Base.green_start
            else:
                return 'stop'

        if place == 28:
            li = Base.in_home_yellow
            if li:
                bead = li[0]
                target = Base.check_place(Base.yellow_start)
                if target != 'e':
                    if bead.color == target.color:
                        return 'stop'
                    else:
                        Base.set_posation(bead,Base.yellow_start,target)
                        li.remove(li[0])
                        return 'move','yellow',Base.yellow_start
                Base.set_posation(bead,Base.yellow_start)
                li.remove(li[0])
                return 'move','yellow',Base.yellow_start
            else:
                return 'stop'
    if place < 25:
        bead = Base.check_place(place)
        print(bead.color)
        print(Person.turn.color)
        if bead.color == Person.turn.color:
            check_w = Bead.check_win(bead,roll)
            if check_w == 'win':
                Base.base[bead.postion-1]='e'
                bead.postion = None
                bead.in_home = True
                Base.li_in_home.append(bead)
                print('win')
                return 'move_win'
            elif check_w == 'stop':
                print('near home')
                return 'stop'


            target = bead.postion + roll
            if target > 24:
                target -= 24
            who_in_target = Base.check_place(target)
            if isinstance(who_in_target,Bead):
                bead_color = bead.color
                color_target = who_in_target.color
                if bead_color == color_target:
                    print('hre stop 99')
                    return 'stop'  
                else:
                    bead.posation = target
                    who_in_target.posation = None
                    Base.set_posation(bead,target,who_in_target)
                    Base.base[place-1]='e'
                    Person.next_turn()
                    return f'move {bead_color} {target} n'
            else:
                bead.posation = target
                Base.set_posation(bead,target)
                Base.base[place-1]='e'
                print(Base.base)
                Person.next_turn()
                print(Person.turn.name)
                return f'move {bead.color} {target} n'

        else:
            print('not owner')
            return 'stop'
            
