from app.extensions import db

class Mark(db.Model):

    mark_id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.game_id'))
    player_name = db.Column(db.String(50))
    row_num = db.Column(db.Integer)
    col_num = db.Column(db.Integer)
    game = db.relationship('Game', backref='marks')



    def __init__(self, player_name, row_num, col_num, game):

        self.player_name = player_name
        self.row_num = row_num
        self.col_num = col_num
        self.game = game

    def __repr__(self):
        return "mark_id: %s\n" \
               "game_id:%s\n " \
               "row_num:%s\n " \
               "col_num:%s\n " \
               "player_name:%s" % (self.mark_id,
                                   self.game_id,
                                   self.row_num,
                                   self.col_num,
                                   self.player_name)