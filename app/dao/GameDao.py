from app.dao.GenericDao import GenericDao
from app.model.GameModel import Game
from app.model.MarkModel import Mark

class GameDao(GenericDao):

    def __init__(self):
        super().__init__()

    def get_games(self):
        all_games = Game.query.all()
        result = self.games_schema.dump(all_games)
        return result

    def get_game(self, game_id):
        game = Game.query.get(game_id)
        result = self.game_schema.dump(game)
        return result

    def create_game(self, player_one_name, player_two_name):
        col_num = 3
        row_num = 3
        new_game = Game(player_one_name, player_two_name)
        self.db.session.add(new_game)
        for i in range(col_num):
            for j in range(row_num):
                new_mark = Mark(None, i, j, new_game)
                self.db.session.add(new_mark)
        self.db.session.commit()
        output = self.game_schema.dump(new_game)
        return output

