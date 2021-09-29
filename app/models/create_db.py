from config import db
from models import Game

games_to_init = [{'game_id':1, 'game_desc': 'Partie 1'},
                 {'game_id':2, 'game_desc': 'Partie 2'}]

db.create_all()


for game in games_to_init:
    g = Game(game_id=game['game_id'], game_desc=game['game_desc'])
    db.session.add(g)


db.session.commit()

