from app.dao.GameDao import GameDao

class GameService:

    def __init__(self):
        self.game_dao = GameDao()

    def get_games(self):
        return self.game_dao.get_games()

    def get_game(self, game_id):
        return self.game_dao.get_game(game_id)

    def create_game(self, player_one_name, player_two_name):
        return self.game_dao.create_game(player_one_name, player_two_name)



