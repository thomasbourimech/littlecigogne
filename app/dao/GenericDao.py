from app.dao.Connection import Connection
from app.schema.GameSchema import GameSchema
from app.schema.GameSchema import MarkSchema


class GenericDao:
    def __init__(self):
        self.db = Connection.get_connection()
        self.mark_schema = MarkSchema()
        self.marks_schema = MarkSchema(many=True)
        self.game_schema = GameSchema()
        self.games_schema = GameSchema(many=True)




