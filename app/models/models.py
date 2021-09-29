from app.models.config import db,ma

class Game(db.Model):

    __tablename__ = 'game'
    game_id = db.Column(db.Integer, primary_key=True)
    game_desc = db.Column(db.String(32))

    def __repr__(self):
        return '<Game id: %s, game desc>' % (self.id, self.game_desc)

class GameSchema(ma.Schema):

    class Meta:
        model = Game
        load_instance = True
        #sqla_session = db.session