from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.model.GameModel import Game
from app.schema.MarkSchema import MarkSchema
from marshmallow_sqlalchemy import fields


class GameSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = Game
    marks = fields.Nested(MarkSchema, many=True)