from flask import jsonify
from flask import request
from service.GameService import GameService
from service.MarkService import MarkService
from service.APIService import APIService
import os
import connexion
from extensions import db

def register_extensions(app):
    db.init_app(app)


connex_app = connexion.FlaskApp(__name__, specification_dir='./')


@connex_app.route('/api/games', methods=['GET'])
def get_games():
     result = GameService().get_games()
     return jsonify(result)

@connex_app.route('/api/games/<game_id>', methods=['GET'])
def get_game(game_id):

     result = GameService().get_game(game_id)
     return jsonify({'game': result}), 200


@connex_app.route('/api/version', methods=['GET'])
def get_version():
    result = APIService().get_version()
    return result

@connex_app.route('/api/games/<game_id>', methods=['PATCH'])
def place_mark(game_id):

    player_name = request.json['player_name']
    col_num = request.json['col_num']
    row_num = request.json['row_num']
    if not MarkService().place_mark(game_id, player_name, col_num, row_num):
        return {"error": "Mark (%s,%s) has already been played" %(col_num, row_num)}, 403

    return {"Ok": "Mark (%s,%s,%s) has been filled by user" % (col_num, row_num, player_name)}, 200



@connex_app.route('/api/games', methods=['POST'])
def create_game():
      player_one_name = request.json['player_one_name']
      player_two_name = request.json['player_two_name']
      output = GameService.create_game(player_one_name, player_two_name)
      return jsonify({'game': output})




connex_app.add_api('yaml.yml')
basedir = os.path.abspath(os.path.dirname(__file__))
connex_app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'tictactoe.db')
connex_app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
register_extensions(connex_app.app)

connex_app.run(debug=True, threaded=True, host="127.0.0.1", port=8080)
