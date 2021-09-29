from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.model.MarkModel import Mark


class MarkSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = Mark
