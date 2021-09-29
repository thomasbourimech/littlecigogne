from flask_sqlalchemy import SQLAlchemy
import os
db = SQLAlchemy()


def init_app(app):
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'tictactoe.db')

    db.init_app(app)

