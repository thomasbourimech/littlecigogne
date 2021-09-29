from app.dao.Connection import Connection
db = Connection.get_connection()

class Game(db.Model):

    game_id = db.Column(db.Integer, primary_key=True)
    player_one_name = db.Column(db.String(50))
    player_two_name = db.Column(db.String(50))
    current_player = db.Column(db.String(50))
    is_over = db.Column(db.Boolean)
    winner = db.Column(db.String(50))

    def __init__(self, player_one_name, player_two_name):
        self.player_one_name = player_one_name
        self.player_two_name = player_two_name

    def __repr__(self):
        return "game_id:%s\n " \
               "player_one_name:%s\n " \
               "player_two_name:%s\n " \
               "is_over:%s" % (self.game_id,
                               self.player_one_name,
                               self.player_two_name,
                               self.is_over)
