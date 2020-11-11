from logic import Base ,Bead, Person

# win
def check_move(roll,bead):
    if bead.ownner == Person.term:
        if not(bead.out and bead.in_home):
            target = bead.position + roll
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
                    Person.term(Person.term)
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
