from logic import Base ,Bead, Person


def check_move(place,roll):
    print('place clicked: ',place)
    if place > 24 :
        if place == 25:
            if roll == 6:
                li = Base.out_blue
                if li and Person.turn.color == 'blue':
                    bead = li[0]
                    target = Base.check_place(Base.blue_start)
                    if target != 'e':
                        if bead.color == target.color:
                            return 'stop blue'
                        else:
                            Base.set_posation(bead,Base.blue_start,target)
                            li.remove(li[0])
                            Person.next_turn()
                            return f'move blue {Base.blue_start} l{target.color}'
                    Base.set_posation(bead,Base.blue_start)
                    li.remove(li[0])
                    Person.next_turn()
                    return f'move blue {Base.blue_start} l'
            # if roll !=6 or out empty or not turn this player
            return 'stop blue'

        elif place == 26:
            if roll == 6:
                li = Base.out_red
                if li and Person.turn.color == 'red':
                    bead = li[0]
                    target = Base.check_place(Base.red_start)
                    if target != 'e':
                        if bead.color == target.color:
                            return 'stop red'
                        else:
                            Base.set_posation(bead,Base.red_start,target)
                            li.remove(li[0])
                            Person.next_turn()
                            return f'move red {Base.red_start} l{target.color}'
                    Base.set_posation(bead,Base.red_start)
                    li.remove(li[0])
                    Person.next_turn()
                    return f'move red {Base.red_start} l'
               
            return 'stop red'
'''  ==========================not complet====================
        elif place == 27:
            li = Base.out_green
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

        elif place == 28:
            li = Base.out_yellow
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
'''
    bead = Base.check_place(place)
    print(Person.turn.color)
    if isinstance(bead,Bead):
        if bead.color == Person.turn.color:
            check_w = Bead.check_win(bead,roll)
            if check_w == 'win':
                Base.base[bead.postion-1]='e'
                bead.postion = None
                bead.in_home = True
                in_home_list = Base.get_list(bead.color,'home')
                in_home_list.append(bead)
                print('win')
                Base.base[place-1]='e'
                Person.next_turn()
                return f'move_win {bead.color}'
            elif check_w == 'stop':
                print('near home')
                return f'stop {bead.color}'


            target = bead.postion + roll
            if target > 24:
                target -= 24
            who_in_target = Base.check_place(target)
            if isinstance(who_in_target,Bead):
                bead_color = bead.color
                color_target = who_in_target.color
                if bead_color == color_target:
                    return f'stop {bead.color}'  
                else:
                    bead.posation = target
                    who_in_target.posation = None
                    Base.set_posation(bead,target,who_in_target)
                    Base.base[place-1]='e'
                    Person.next_turn()
                    return f'move {bead_color} {target} n{who_in_target.color}'
            else:
                bead.posation = target
                Base.set_posation(bead,target)
                Base.base[place-1]='e'
                print(Base.base)
                Person.next_turn()
                print(Person.turn.name)
                print('inhome',Base.in_home_blue,Base.in_home_red)
                return f'move {bead.color} {target} n'

        else:
            print('not owner')
            return f'stop'
    else:
        print('empety home')    
        return f'stop'

def moveable(color,roll):
        for bead_in_map in Base.base:
            if isinstance(bead_in_map,Bead):
                if bead_in_map.color == color:
                    if Bead.check_win(bead_in_map,roll) == 'move':
                        target = bead_in_map.postion + roll
                        if target > 24:
                            target -= 24
                        bead_in_target = Base.check_place(target)
                        if isinstance(bead_in_target,Bead):
                            if bead_in_target.color != bead_in_map.color:
                                return True
                        else:
                            return True
        li = Base.get_list(color,'out')
        if li and roll == 6:
            return True
        return False


