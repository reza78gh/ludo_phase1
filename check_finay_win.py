from logic import Person, Base

def finaly_win():
    for player in Person.player_li:
        if len(Base.get_list(player.color, 'home')) == 4:
            return player
    else:
        return None
    