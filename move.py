from logic import Base ,Bead, Person

# todo: check win
def check_move(roll,bead):
    if bead.ownner == Person.turn:
        if not(bead.out and bead.in_home):
            check_w = Bead.check_win(bead,roll)
            if check_w == 'win':
                Base.base[bead.postion]='e'
                bead.postion = None
                bead.in_home = True
                Base.li_in_home.append(bead)
                # move pyqt
                return
            elif check_w == 'stop':
                # again
                return

            target = bead.position + roll
            if target > 24:
                target -= 24
            who_in_target = Base.check_place(target)
            if isinstance(who_in_target,Bead):
                bead_color = bead.color
                color_target = who_in_target.color
                if bead_color == color_target:
                    pass
                    # todo: error
                else:
                    bead.posation = target
                    who_in_target.posation = None
                    Base.set_posation(bead,target,who_in_target)
                    Person.next_turn()
                    # todo: remov enemy bead
            else:
                bead.posation = target
                Base.set_posation(bead,target)
                    # todo: move
                
        else:
            if roll == 6 and bead.out == True:
                bead.set_posation()
            #not in game
    else:
        # not owner
        pass
