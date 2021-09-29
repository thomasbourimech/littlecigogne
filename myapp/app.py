from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy import fields
import os


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'tictactoe.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Game(db.Model):

    game_id = db.Column(db.Integer, primary_key=True)
    player_one_name = db.Column(db.String(50))
    player_two_name = db.Column(db.String(50))
    """
    game_status:
    1 -> won by player 1
    2 -> won by player 2
    0 -> draw
    None -> playing
    """
    game_status = db.Column(db.Integer)


    def __init__(self, player_one_name, player_two_name):
        self.player_one_name = player_one_name
        self.player_two_name = player_two_name

    def __repr__(self):
        return "game_id:%s\n " \
               "player_one_name:%s\n " \
               "player_two_name:%s\n " \
               "game_status:%s" % (self.game_id,
                                   self.player_one_name,
                                   self.player_two_name,
                                   self.game_status)


class Mark(db.Model):

    mark_id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.game_id'))
    player_name = db.Column(db.String(50))
    row_num = db.Column(db.Integer)
    col_num = db.Column(db.Integer)
    game = db.relationship('Game', backref='Marks')



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



class MarkSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = Mark


mark_schema = MarkSchema()
marks_schema = MarkSchema(many=True)

class GameSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = Game
    Marks = fields.Nested(MarkSchema, many=True)


game_schema = GameSchema()
games_schema = GameSchema(many=True)


@app.route('/games', methods=['GET'])
def get_games():
    all_games = Game.query.all()
    result = games_schema.dump(all_games)
    return jsonify(result)


@app.route('/games/<game_id>', methods=['GET'])
def get_game(game_id):
    game = Game.query.get(game_id)
    game_schema = GameSchema()
    output = game_schema.dump(game)
    return jsonify({'user': output})

@app.route('/version', methods=['GET'])
def get_version():
    return {"version": 1.0}

@app.route('/games/<game_id>', methods=['PATCH'])
def place_mark(game_id):

    player_name = request.json['player_name']
    col_num = request.json['col_num']
    row_num = request.json['row_num']
    game_to_update = Game.query.get(game_id)
    mark_to_update = db.session.query(Mark).filter(Mark.col_num == col_num).\
        filter(Mark.row_num == row_num).\
        filter(Mark.game_id == game_id).first()

    if mark_to_update.player_name is None:
        return {"toto", 400}


@app.route('/games', methods=['POST'])
def create_game():
    col_num = 3
    row_num = 3

    player_one_name = request.json['player_one_name']
    player_two_name = request.json['player_two_name']
    new_game = Game(player_one_name, player_two_name)
    db.session.add(new_game)


    for i in range(col_num):
        for j in range(row_num):
            new_mark = Mark(new_game.game_id, None, i, j, new_game)
            db.session.add(new_mark)

    db.session.commit()

    game_schema = GameSchema()
    output = game_schema.dump(new_game)
    return jsonify({'game': output})



if __name__ == '__main__':
    app.run(host='localhost',port='8080',debug=True)
