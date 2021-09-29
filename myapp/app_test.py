from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy import fields
import os


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///' + os.path.join(basedir, 'app2.db')

db = SQLAlchemy(app)
ma = Marshmallow(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))


class Reward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reward_name = db.Column(db.String(250))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='rewards')



class RewardSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Reward

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
    rewards = fields.Nested(RewardSchema, many=True)


@app.route('/')
def index():
    one_user = User.query.first()

    user_schema = UserSchema()
    output = user_schema.dump(one_user)

    return jsonify({'user': output})

if __name__== '__main__':
    app.run(debug=True)