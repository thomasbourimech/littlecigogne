from app.models.models import Game, GameSchema
from flask import jsonify, make_response
import json
import logging

def get_version():
    return {"version": 1.0}

def create_game():
    pass

def get_game(game_id):

    game = Game.query.order_by(Game.game_id).all()
    game_schema = GameSchema(many=True)
    data = game_schema.dump(game)
    return data


def place_mark(game_id, mark):
    pass
